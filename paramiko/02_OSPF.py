import paramiko
import time
import getpass
ssh_client = paramiko.SSHClient()

# Bypass part of accept key and so on.
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())



password = getpass.getpass('Enter password: ')
r1 = {'hostname':'192.168.88.244', 'port':'22', 'username':'maicon', 'password': password}
r2 = {'hostname':'192.168.88.237', 'port':'22', 'username':'maicon', 'password': password}
r3 = {'hostname':'192.168.88.236', 'port':'22', 'username':'maicon', 'password': password}

routers = [r1, r2, r3]


for router in routers:

    print(f'Connecting to {router["hostname"]}')
    ssh_client.connect(**router, look_for_keys=False, allow_agent=False)
    shell = ssh_client.invoke_shell()


    shell.send('enable\n')
    shell.send('12345\n')
    shell.send('conf t\n')
    shell.send('router ospf 1\n')
    shell.send('net 0.0.0.0 0.0.0.0 area 0\n')
    shell.send('end\n')
    shell.send('terminal length 0\n')
    shell.send('sh ip protocols\n')
    time.sleep(2)


    output = shell.recv(10000).decode()
    print(output)
    time.sleep(5)