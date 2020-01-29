import paramiko
import sys
# print(sys.argv[1])
# exit()

key = paramiko.RSAKey.from_private_key_file("C:/RLN/Dev/ElevationBC/Elevation_Week11/SSH/rsa_private_key.pem")
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
print("Connecting")
client.connect(hostname="ec2-52-59-204-217.eu-central-1.compute.amazonaws.com", username="ubuntu", pkey=key)
print("Connected")

def dirs_files(my_full_name, my_dir_name, my_file_name):
    client.exec_command('chmod 400 rsa_private_key.pem')
    print('creating new folder:')
    client.exec_command(f'mkdir {my_full_name}')
    print('creating 9 new files in 8 new folders:')
    for i in range(1, 9):
        print(f'folder num {i}')
        command_a = f'cd {my_full_name} \nmkdir {my_dir_name}{i}'
        client.exec_command(command_a)
        for j in range(1, 10):
            print(f'file num: {j}')
            command_b = f'cd {my_full_name} \n cd {my_dir_name}{i} \n touch {my_file_name}{j}.py'
            client.exec_command(command_b)

    client.close()

# dirs_files('RebeccaNahom', 'Rebecca', 'Nahom')
dirs_files(sys.argv[1], sys.argv[2], sys.argv[3])