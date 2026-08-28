#STeps

# Step1: export SSH_PASSWORD
# STep 2: execute script with all cmd-line args
# check-uptime-basic.py 192.168.1.13 musharaf_manzoor
# Task: check-uptime-basic.py usr_name 192.168.1.13  192.168.1.22 192.168.1.12
# v_auto/ verventech@123 -> make it passwordless sudo
import sys
import os
import paramiko

# Ensure correct number of arguments are passed
if len(sys.argv) < 3:
    print("Usage: python check_uptime.py <hostname> <username>")
    sys.exit(1)

hostname = sys.argv[1]
username = sys.argv[2]
password = os.getenv('SSH_PASSWORD') # export SSH_PASSWORD="your-pass"

if not password:
    print("Error: SSH_PASSWORD environment variable is not set.", file=sys.stderr)
    sys.exit(1)

# Initialize and connect SSH client
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy()) #Auto add cert as "yes"

try:
    client.connect(hostname, username=username, password=password)
    
    # Run the commandpw
    stdin, stdout, stderr = client.exec_command('uptime')
    
    output = stdout.read().decode('utf-8').strip()
    error = stderr.read().decode('utf-8').strip()
    
    if output:
        print(f"[{hostname}] {output}")
    if error:
        print(f"[{hostname}] Error: {error}", file=sys.stderr)

except Exception as e:
    print(f"Connection failed: {e}", file=sys.stderr)
finally:
    client.close()