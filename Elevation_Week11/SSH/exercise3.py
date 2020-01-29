import paramiko

key = paramiko.RSAKey.from_private_key_file("C:/RLN/Dev/ElevationBC/Elevation_Week11/SSH/rsa_private_key.pem")
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
print("Connecting")
client.connect(hostname="ec2-52-59-204-217.eu-central-1.compute.amazonaws.com", username="ubuntu", pkey=key)
print("Connected")

def printDirsNamesAlphabetical():
    command = f'ls -d */'
    stdin, stdout, stderr = client.exec_command(command)
    dirs = str(stdout.read()).split("/\\n")
    alpha_dirs = sorted(dirs, key=lambda v: v.upper())
    print(alpha_dirs)
    with open("dirsNames.txt", "w") as the_file:
        the_file.write('\n'.join(alpha_dirs))
    client.close()

printDirsNamesAlphabetical()


