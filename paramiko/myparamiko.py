import paramiko
import time


def connect(server_ip, server_port, user, passwd):
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy)

    print(f'Connecting to {server_ip}')
    ssh_client.connect(hostname=server_ip, port=server_port, username=user, password=passwd, look_for_keys=False, allow_agent=False)

    return ssh_client




def get_shell(ssh_client):
    shell = ssh_client.invoke_shell()
    return shell



def send_command(shell, command, timout=1):
    print(f'Sendind command: {command}')
    shell.send(command + '\n')
    time.sleep(timout)



def show(shell, n=10000):
    output = shell.recv(n)
    return output.decode() 




def close(ssh_client):
    if ssh_client.get_transport().is_active() == True:
        print('Close Connection')
        ssh_client.close() 



if __name__ == '__main__':

    router = {'server_ip':'192.168.88.244', 'server_port':'22', 'user':'#####', 'passwd': '#####'}
    client = connect(**router)
    shell = get_shell(client)


    send_command(shell, 'enable')
    send_command(shell, '#####')
    send_command(shell, 'terminal len 0')
    send_command(shell, 'sh version')
    send_command(shell, 'sh ip int brief')


    output = show(shell)
    print(output)