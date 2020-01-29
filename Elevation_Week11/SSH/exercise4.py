import paramiko

key = paramiko.RSAKey.from_private_key_file("C:/RLN/Dev/ElevationBC/Elevation_Week11/SSH/rsa_private_key.pem")
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
print("Connecting")
client.connect(hostname="ec2-52-59-204-217.eu-central-1.compute.amazonaws.com", username="ubuntu", pkey=key)
print("Connected")


def isDiff(firstFile, secondFile):
    command = f'diff {firstFile}/firstFile.txt {secondFile}/secondFile.txt'
    stdin, stdout, stderr = client.exec_command(command)
    if stdout.read():
        print('True. Files are diff')
    else:
        print('False. Files are not diff')
    client.close()

isDiff('/home/ubuntu/firstFile', '/home/ubuntu/secondFile/secondFile')