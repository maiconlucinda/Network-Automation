from nornir import InitNornir
from nornir_napalm.plugins.tasks import napalm_ping
from nornir_utils.plugins.functions import print_result


nr = InitNornir(config_file="config.yaml")


def ping_test(task):
    task.run(napalm_ping, dest="192.168.88.1")


results = nr.run(task=ping_test)
print_result(results)