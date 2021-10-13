import requests


class NovoServeApi:
    def __init__(self, username, api_key):
        self.username = username
        self.api_key = api_key
        self.api_url = "https://api.novoserve.com/"

    def __post(self, endpoint, post_data):
        response = requests.post(self.api_url + endpoint, auth=(self.username, self.api_key), data=post_data)
        return response.json()

    def __get(self, endpoint):
        response = requests.get(self.api_url + endpoint, auth=(self.username, self.api_key))
        return response.json()

    def __delete(self, endpoint):
        response = requests.delete(self.api_url + endpoint, auth=(self.username, self.api_key))
        return response.json()

    def get_bandwidth(self, server_id):
        return self.__get("bandwidth/" + server_id)

    def get_powerstate(self, server_id):
        return self.__get("powerstate/" + server_id)

    def power_on(self, server_id):
        return self.__post("powerstate/" + server_id, {"action": "poweron"})

    def power_off(self, server_id):
        return self.__post("powerstate/" + server_id, {"action": "poweroff"})

    def reboot(self, server_id):
        return self.__post("powerstate/" + server_id, {"action": "reset"})

    def cold_boot(self, server_id):
        return self.__post("powerstate/" + server_id, {"action": "coldboot"})

    def get_console_url(self, server_id, ip_address):
        return self.__post("console-url/" + server_id, {"remoteIp": ip_address})

    def get_server(self, server_id):
        return self.__get("servers/" + server_id)

    def get_all_servers(self):
        return self.__get("servers/")

    def get_webiso_options(self):
        return self.__get("webiso-installs/")

    def get_webiso(self, server_id):
        return self.__get("webiso-installs/" + server_id)

    def set_webiso(self, server_id, webiso_url):
        return self.__post("webiso-installs/" + server_id, {"url": webiso_url})

    def delete_webiso(self, server_id):
        return self.__delete("webiso-installs/" + server_id)
