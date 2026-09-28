pre-req:

1.Create the 'vansible' user on the target Ubuntu server- jenkins-vm
sudo useradd -m -s /bin/bash vansible
sudo usermod -aG sudo vansible
echo "vansible ALL=(ALL) NOPASSWD:ALL" | sudo tee /etc/sudoers.d/vansible
sudo chmod 0440 /etc/sudoers.d/vansible

2.Generate SSH key pair on Ansible Control Node:
ssh-keygen -t ed25519 -C "ansible-control-node"

3. push the key to the vansible user on the target server 
ssh-copy-id vansible@192.168.1.100

4.Test keyless SSH connection
ssh vansible@192.168.1.100