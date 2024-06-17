
import paramiko
import time
import getpass
ssh_client = paramiko.SSHClient()
# Bypass part of accept key and so on.
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())



# ssh_client.connect(hostname='192.168.88.244', port='22', 
#                    username="maicon", password="12345", look_for_keys=False, allow_agent=False)


password = getpass.getpass('Enter password: ')
router = {'hostname':'192.168.88.244', 'port':'22', 'username':'maicon', 'password': password}
print(f'Connecting to {router["hostname"]}')
ssh_client.connect(**router, look_for_keys=False, allow_agent=False)


shell = ssh_client.invoke_shell()
shell.send('terminal length 0\n')
shell.send('show version\n')
time.sleep(1)

shell.send('enable\n')
time.sleep(1)
shell.send(f'{password}\n')
time.sleep(1)
shell.send('show ip int brief\n')
time.sleep(1)

output = shell.recv(10000)
output = output.decode('utf-8')
print(output)







if ssh_client.get_transport().is_active() == True:
    print('Close Connection')
    ssh_client.close()