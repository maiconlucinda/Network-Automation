from nornir import InitNornir
from nornir_napalm.plugins.tasks import napalm_get
from nornir_utils.plugins.functions import print_result


nr = InitNornir(config_file="config.yaml")


def napalm_getters(task):
    task.run(napalm_get, getters=["get_interfaces", "get_facts"])


results = nr.run(task=napalm_getters)
print_result(results)