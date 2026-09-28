enkins CI/CD Infrastructure Setup & Teardown Guide
This repository contains Ansible playbooks to provision, manage, and deep-purge an end-to-end Jenkins CI/CD environment comprising a Jenkins Master VM and two target deployment environments: Staging (192.168.1.36) and Production (192.168.1.35).

🏗️ Architecture & Authentication Flow
Control Server (localhost): Runs Ansible playbooks to provision all nodes.

Jenkins Master VM: Runs Java 21, Jenkins, and Docker Engine. Generates a dedicated SSH keypair (/var/lib/jenkins/.ssh/id_rsa) under the jenkins system account.

Target VMs (Staging / Production): Configured with Docker Engine, a verjenkins deployment user in the docker group, and passwordless sudo rights.

Passwordless SSH Auth: The jenkins user on the Master VM authenticates to verjenkins@<target-ip> via the injected SSH public key without requiring passwords.

📋 Step 1: Control Node Setup (Localhost)
Before executing playbooks, install Ansible dependencies (specifically python3-passlib for sha512 password hashing) on the control node.

Bash
# Prepare control node dependencies
ansible-playbook setup-localhost.yml -K
🚀 Step 2: Jenkins Master Setup
Provision OpenJDK 21, Docker Engine, and Jenkins LTS using official debian-stable keyrings, and generate the pipeline SSH keypair.

Bash
# Provision Jenkins Master VM
ansible-playbook -i hosts.ini setup-jenkins.yml
Get the Generated Public Key & Initial Password
Bash
# 1. Read initial Jenkins admin password
sudo cat /var/lib/jenkins/secrets/initialAdminPassword

# 2. Display the generated Jenkins public SSH key (copy this for target VM prompts)
sudo cat /var/lib/jenkins/.ssh/id_rsa.pub
🎯 Step 3: Staging & Production Target Environment Setup
Provision Docker Engine, set up the verjenkins deployment user, configure passwordless sudo (/etc/sudoers.d/verjenkins), and inject the Jenkins SSH public key.

Provision Staging (192.168.1.36)
Bash
ansible-playbook -i hosts.ini setup-staging.yml
Prompts:

Paste the Jenkins public SSH key (cat /var/lib/jenkins/.ssh/id_rsa.pub).

Enter the password for the verjenkins target user.

Provision Production (192.168.1.35)
Bash
ansible-playbook -i hosts.ini setup-production.yml
Prompts:

Paste the Jenkins public SSH key (cat /var/lib/jenkins/.ssh/id_rsa.pub).

Enter the password for the verjenkins target user.

🔑 Step 4: Verify Passwordless SSH Authentication
Test SSH connectivity directly from the jenkins system account on the Jenkins Master VM to the target nodes:

Bash
# 1. Switch to the jenkins system account context on Jenkins VM
sudo su - jenkins

# 2. Verify passwordless SSH and Docker execution on Staging
ssh verjenkins@192.168.1.36 "docker ps && sudo whoami"

# 3. Verify passwordless SSH and Docker execution on Production
ssh verjenkins@192.168.1.35 "docker ps && sudo whoami"
Expected Output: Docker container listing followed by root (confirming keyless auth and passwordless sudo access).

🧹 Teardown & Purge Commands
To completely reset any environment, stop containers, purge Docker system resources, remove workspace artifacts, and clear package index caches.

Purge Staging Environment
Bash
ansible-playbook -i hosts.ini prune-staging.yml
Purge Production Environment
Bash
ansible-playbook -i hosts.ini prune-production.yml
Purge Jenkins Master Environment
Bash
ansible-playbook -i hosts.ini prune-jenkins.yml