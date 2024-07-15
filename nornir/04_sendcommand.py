from nornir import InitNornir
from nornir_scrapli.tasks import send_command
from nornir_utils.plugins.functions import print_result


nr = InitNornir(config_file="config.yaml")


command_list = ["show ip interface brief"]
def show_command_test(task):
    for command in command_list:
        print(type(task))
        task.run(task=send_command, command=command)

results = nr.run(show_command_test)
print_result(results)