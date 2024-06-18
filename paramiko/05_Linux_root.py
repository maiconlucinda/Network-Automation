import paramiko
import time
import getpass
ssh_client = paramiko.SSHClient()

ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
password = getpass.getpass('Enter password: ')
linux = {'hostname':'192.168.88.235', 'port':'22', 'username':'#######', 'password': password}



print(f'Connecting to {linux["hostname"]}')
ssh_client.connect(**linux, look_for_keys=False, allow_agent=False)


stdin, stdout, stderr = ssh_client.exec_command('sudo useradd ######\n', get_pty=True)
stdin.write('########\n')
time.sleep(2)
#print(stderr.read().decode())


stdin, stdout, stderr = ssh_client.exec_command('cat /etc/passwd\n')
print(stdout.read().decode())
time.sleep(1)




if ssh_client.get_transport().is_active() == True:
    print('Close Connection')
    ssh_client.close()