Standalone playbook named setup-localhost.yml that automatically installs python3-passlib and all required dependencies on your control machine (localhost) so you don't have to run manual pip or apt commands.

Pass the --ask-become-pass (-K) Flag (Easiest)
Add -K when running the playbook. Ansible will prompt you interactively for your sudo password:

Bash
ansible-playbook setup-localhost.yml -K