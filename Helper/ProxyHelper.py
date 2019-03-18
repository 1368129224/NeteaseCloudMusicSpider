import requests
import fake_useragent

def get_proxy():
    return requests.get("http://118.24.52.95:5010/get/").content

def delete_proxy(proxy):
    requests.get("http://118.24.52.95:5010/delete/?proxy={}".format(proxy))

def getValidProxy():
    ua = fake_useragent.UserAgent()
    headers = {
        'User-Agent': ua.chrome
    }
    proxy = get_proxy().decode("utf8")
    while True:
        retry_count = 5
        try:
            if retry_count <= 0:
                proxy = get_proxy().decode("utf8")
            html = requests.get("http://checkip.dns.he.net/", proxies={"http": "http://{}".format(proxy)}, headers=headers, timeout=6)
            if html.status_code == 200:
                return "http://{}".format(proxy)
        except:
            retry_count -= 1
