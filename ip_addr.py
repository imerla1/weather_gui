from requests import get

def get_ipaddress():
    return get('https://ipapi.co/ip/').text
