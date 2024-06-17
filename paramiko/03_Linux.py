
import paramiko
import time
import getpass 
ssh_client = paramiko.SSHClient()


ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

password = getpass.getpass('Enter password: ')
linux = {'hostname':'192.168.88.241', 'port':'22', 'username':'guguadmin', 'password': password}



print(f'Connecting to {linux["hostname"]}')
ssh_client.connect(**linux, look_for_keys=False, allow_agent=False)
shell = ssh_client.invoke_shell()


shell.send('cat /etc/shadow\n')
#shell.send("")
time.sleep(1)


output = shell.recv(10000).decode('utf-8')
print(output)
time.sleep(5)

