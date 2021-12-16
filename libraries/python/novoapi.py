import requests


class NovoServeApi:
    def __init__(self, username: str, api_key: str):
        self.username = username
        self.api_key = api_key
        self.api_url = "https://api.novoserve.com/v0/"

    # Private functions to do HTTP requests
    def __post(self, endpoint: str, post_data: dict = None) -> dict:
        if post_data is None:
            post_data = {}
        response = requests.post(self.api_url + endpoint, auth=(self.username, self.api_key), json=post_data)
        return self.__check_api_response(response.json())

    def __get(self, endpoint: str) -> dict:
        response = requests.get(self.api_url + endpoint, auth=(self.username, self.api_key))
        return self.__check_api_response(response.json())

    def __delete(self, endpoint: str) -> dict:
        response = requests.delete(self.api_url + endpoint, auth=(self.username, self.api_key))
        return self.__check_api_response(response.json())

    def __check_api_response(self, response: dict) -> dict:
        if response['status'] == 'success':
            return response['results']
        elif 'status' in response and 'results' in response:
            raise ApiError('[' + response['status'] + '] ' + response['results'])
        else:
            raise ApiError('Unknown error: ' + str(response))

    # Public functions to call specific endpoints
    def get_all_servers(self) -> dict:
        return self.__get("servers/")

    def get_server(self, server_id: str) -> dict:
        return self.__get("servers/" + server_id)

    def get_power_state(self, server_id: str) -> dict:
        return self.__get("servers/" + server_id + "/power")

    def power_on(self, server_id: str) -> dict:
        return self.__post("servers/" + server_id + "/poweron")

    def power_off(self, server_id: str) -> dict:
        return self.__post("servers/" + server_id + "/poweroff")

    def reboot(self, server_id: str) -> dict:
        return self.__post("servers/" + server_id + "/reset")

    def cold_boot(self, server_id: str) -> dict:
        return self.__post("servers/" + server_id + "/power", {"action": "coldboot"})

    def get_bandwidth_usage(self, server_id: str) -> dict:
        return self.__get("servers/" + server_id + "/bandwidth")

    def get_bandwidth_graph(self, server_id: str) -> dict:
        return self.__get("servers/" + server_id + "/bandwidth/graph")

    def get_cancellation(self, server_id: str) -> dict:
        return self.__get("servers/" + server_id + "/cancellation")

    def request_cancellation(self, server_id: str) -> dict:
        return self.__post("servers/" + server_id + "/cancellation")

    def get_ipmi_link(self, server_id: str, ip_address: str, whitelabel: str = "no") -> dict:
        return self.__post("servers/" + server_id + "/ipmi-link", {"remoteIp": ip_address, "whitelabel": whitelabel})

    def get_virtual_media(self, server_id: str) -> dict:
        return self.__get("servers/" + server_id + "/virtual-media")

    def mount_virtual_media(self, server_id: str, virtual_media_url: str) -> dict:
        return self.__post("servers/" + server_id + "/virtual-media", {"url": virtual_media_url})

    def unmount_virtual_media(self, server_id: str) -> dict:
        return self.__delete("servers/" + server_id + "/virtual-media")

    def get_virtual_media_images(self, server_id: str) -> dict:
        return self.__get("servers/" + server_id + "/virtual-media/images")

    def get_network_config(self, server_id: str) -> dict:
        return self.__get("servers/" + server_id + "/network-config")

    def set_network_config(self, server_id: str, post_data: dict) -> dict:
        return self.__post("servers/" + server_id + "/network-config", post_data)

    def get_l2_domains(self) -> dict:
        return self.__get("l2-domains/")

    def get_l2_domain(self, l2_domain_id: int) -> dict:
        return self.__get("l2-domains/" + str(l2_domain_id))

    def set_l2_domain_name(self, l2_domain_id: int, l2_domain_name: str) -> dict:
        return self.__post("l2-domains/" + str(l2_domain_id), {"name": l2_domain_name})

    def get_networks(self) -> dict:
        return self.__get("networks/")

    def get_network(self, network_id: int) -> dict:
        return self.__get("networks/" + str(network_id))

    def set_network_name(self, network_id: int, network_name: str) -> dict:
        return self.__post("networks/" + str(network_id), {"name": network_name})

    def get_rdns_records(self) -> dict:
        return self.__get("networks/rdns/")

    def set_rdns_record(self, ip: str, record: str) -> dict:
        return self.__post("networks/rdns/", {"ip": ip, "record": record})

    def get_rdns_records_for_network(self, network_id: int) -> dict:
        return self.__get("networks/" + str(network_id) + "/rdns")

    def get_rdns_record(self, rdns_id: int) -> dict:
        return self.__get("networks/rdns/" + str(rdns_id))

    def delete_rdns_record(self, rdns_id: int) -> dict:
        return self.__delete("networks/rdns/" + str(rdns_id))


class ApiError(Exception):
    pass
