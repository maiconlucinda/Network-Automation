
import myparamiko


client = myparamiko.connect('192.168.88.235', '22', '#####', '######')
shell = myparamiko.get_shell(client)

myparamiko.send_command(shell, 'uname -a')
output = myparamiko.show(shell)
print(output)


myparamiko.close(client)