from nornir import InitNornir
from nornir_scrapli.tasks import send_commands
from nornir_utils.plugins.functions import print_result


nr = InitNornir(config_file="config.yaml")


def show_command_test(task):
    task.run(task=send_commands, commands=["show ip interface brief", "show version", "show runn"])

results = nr.run(show_command_test)
print_result(results)