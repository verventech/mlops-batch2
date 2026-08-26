import subprocess

#subprocess.run(["cat", "requirements.txt"])


subprocess.run("cat requirements.txt", shell=True)
subprocess.run("ping 192.168.1.1 -c 5", shell=True)