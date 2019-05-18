import requests
from fake_useragent import UserAgent
from Helper.ApiHelper import api

def testa(api):
    url = 'http://localhost:3000/comment/music?id=210049&limit=100&offset='
    ua = UserAgent()
    api.startApi()
    headers = {
        'UserAgent': ua.random
    }
    try:
        for i in range(0, 26000, 100):
            resp = requests.get(url=url + str(i), headers=headers)
            print(i, resp.status_code, resp.json()['code'])
    finally:
        api.stopApi()