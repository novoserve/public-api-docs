import requests


class NovoServeApi:
    def __init__(self, username, api_key):
        self.username = username
        self.api_key = api_key
        self.api_url = "https://api.novoserve.com/v0/"

    # Private functions to do HTTP requests
    def __post(self, endpoint, post_data=None):
        if post_data is None:
            post_data = {}
        response = requests.post(self.api_url + endpoint, auth=(self.username, self.api_key), data=post_data)
        return response.json()

    def __get(self, endpoint):
        response = requests.get(self.api_url + endpoint, auth=(self.username, self.api_key))
        return response.json()

    def __delete(self, endpoint):
        response = requests.delete(self.api_url + endpoint, auth=(self.username, self.api_key))
        return response.json()

    # Public functions to call specific endpoints
    def get_all_servers(self):
        return self.__get("servers/")

    def get_server(self, server_id):
        return self.__get("servers/" + server_id)

    def get_power_state(self, server_id):
        return self.__get("servers/" + server_id + "/power")

    def power_on(self, server_id):
        return self.__post("servers/" + server_id + "/power", {"action": "poweron"})

    def power_off(self, server_id):
        return self.__post("servers/" + server_id + "/power", {"action": "poweroff"})

    def reboot(self, server_id):
        return self.__post("servers/" + server_id + "/power", {"action": "reset"})

    def cold_boot(self, server_id):
        return self.__post("servers/" + server_id + "/power", {"action": "coldboot"})

    def get_bandwidth_usage(self, server_id):
        return self.__get("servers/" + server_id + "/bandwidth")

    def get_cancellation(self, server_id):
        return self.__get("servers/" + server_id + "/cancellation")

    def request_cancellation(self, server_id):
        return self.__post("servers/" + server_id + "/cancellation")

    def get_ipmi_link(self, server_id, ip_address, whitelabel="no"):
        return self.__post("servers/" + server_id + "/ipmi-link", {"remoteIp": ip_address, "whitelabel": whitelabel})

    def get_virtual_media(self, server_id):
        return self.__get("servers/" + server_id + "/virtual-media")

    def mount_virtual_media(self, server_id, virtual_media_url):
        return self.__post("servers/" + server_id + "/virtual-media", {"url": virtual_media_url})

    def unmount_virtual_media(self, server_id):
        return self.__delete("servers/" + server_id + "/virtual-media")

    def get_virtual_media_images(self, server_id):
        return self.__get("servers/" + server_id + "/virtual-media/images")
