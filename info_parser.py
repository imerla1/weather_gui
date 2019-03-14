class Info:
    def __init__(self):
        self.city = ''
        self.country = ''

    def get_personal_info(self):
        import requests
        import json
        from ip_addr import get_ipaddress
        ip_addr = str(get_ipaddress())
        url = 'http://ip-api.com/json/{}'
        req=requests.get(url.format(ip_addr))


        x = req.json()

        dict_mapping = {}

        for i in x:
            self.city = x['city']
            self.country = x['country']
            dict_mapping[i] = x[i]

        return dict_mapping
