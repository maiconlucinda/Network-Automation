from nornir import InitNornir
from nornir_netmiko.tasks import netmiko_send_config
from nornir_utils.plugins.functions import print_result


nr = InitNornir(config_file="config.yaml")



commands_list = ["ntp server 11.22.11.22"]

def recursive_send_config(task):
    task.run(netmiko_send_config, config_commands=commands_list)


results = nr.run(task=recursive_send_config)
print_result(results)