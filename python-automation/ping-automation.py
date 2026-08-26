import subprocess

servers = [
    "192.168.1.1",
    "192.168.1.13",
    "google.com",
    "yahoo.com",
    "192.168.1.201",
    "10.0.0.1"
]

print ("Starting the script to check all servers")

for server in servers:
    result = subprocess.run(["ping", "-c", "2", server], capture_output=True, text=True)

    #returncode 0 means ping is successful 0 means success
    
    if result.returncode== 0:
        print(f"{server} is UP!")
    else:
        print(f"{server} is DOWN!!!")


