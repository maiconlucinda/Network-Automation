import myparamiko
from datetime import datetime
import threading

def backup(router):

    client = myparamiko.connect(**router)
    shell = myparamiko.get_shell(client)


    myparamiko.send_command(shell, 'terminal length 0')
    myparamiko.send_command(shell, 'enable')
    myparamiko.send_command(shell, '#####')
    myparamiko.send_command(shell, 'show run')

    output = myparamiko.show(shell)
    print(output)

    # Create a list from lines
    output_list = output.splitlines()

    output_list = output_list[11:-1]


    # Create a string from a list
    output = '\n'.join(output_list)
    #print(output)


    now = datetime.now()
    year = now.year
    month = now.month
    day = now.day
    hour = now.hour
    minute = now.minute

    with open(f'archives/`{router["server_ip"]}_{year}-{month}-{day}.txt', 'w') as f:
        f.write(output)


    myparamiko.close(client)





router1 = {'server_ip':'192.168.88.244', 'server_port':'22', 'user':'#####', 'passwd':'#####'}
router2 = {'server_ip':'192.168.88.237', 'server_port':'22', 'user':'#####', 'passwd':'#####'}
router3 = {'server_ip':'192.168.88.236', 'server_port':'22', 'user':'#####', 'passwd':'#####'}

routers = [router1, router2, router3]

threads = []
for router in routers:
    th = threading.Thread(target=backup, args=(router,))
    threads.append(th)


for th in threads:
    th.start()


for th in threads:
    th.join()