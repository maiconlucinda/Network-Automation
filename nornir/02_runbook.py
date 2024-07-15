# This one has to be imported
from nornir import InitNornir

# This one is used to send command (enable mode for example)
from nornir_scrapli.tasks import send_command

# This one is used to send config in the "conf ter" mode
from nornir_scrapli.tasks import send_config

# This is one is to print result
from nornir_utils.plugins.functions import print_result




# Inicialising our "nr" object
nr = InitNornir(config_file="config.yaml")

def random_config(task):
    task.run(task=send_config, config=f"ntp server {task.host['ntp_server']}")


results = nr.run(task=random_config)
print_result(results)