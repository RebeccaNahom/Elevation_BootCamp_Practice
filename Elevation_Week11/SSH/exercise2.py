import paramiko

key = paramiko.RSAKey.from_private_key_file("C:/RLN/Dev/ElevationBC/Elevation_Week11/SSH/rsa_private_key.pem")
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
print("Connecting")
client.connect(hostname="ec2-52-59-204-217.eu-central-1.compute.amazonaws.com", username="ubuntu", pkey=key)
print("Connected")

def print_is():
    command = f'cd a \ncd b \ncd c \ncd d \n grep is secretFile.txt'
    stdin, stdout, stderr = client.exec_command(command)
    print(stdout.read())
    client.close()

print_is()

