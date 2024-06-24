import myparamiko
from datetime import datetime
import threading


def showuser(router):

    ssh_client = myparamiko.connect(**router)
    shell = myparamiko.get_shell(ssh_client)

    myparamiko.send_command(shell, 'terminal length 0')
    myparamiko.send_command(shell, 'enable')
    myparamiko.send_command(shell, '####')
    myparamiko.send_command(shell, 'show users')


    output = myparamiko.show(shell)
    print(output)


router1 = {'server_ip':'192.168.88.244', 'server_port':'22', 'user':'#####', 'passwd':'#####'}
router2 = {'server_ip':'192.168.88.237', 'server_port':'22', 'user':'#####', 'passwd':'#####'}
router3 = {'server_ip':'192.168.88.236', 'server_port':'22', 'user':'#####', 'passwd':'#####'}

routers = [router1, router2, router3]

threads = []
for router in routers:
    th = threading.Thread(target=showuser, args=(router,))
    threads.append(th)

for th in threads:
    th.start()

for th in threads:
    th.join()

