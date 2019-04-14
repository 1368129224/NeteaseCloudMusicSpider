import requests
from fake_useragent import UserAgent


ua = UserAgent()
headers = {
    'UserAgent':ua.chrome
}
url = r'http://localhost:3000/playlist/catlist'
json = requests.get(url,headers).json()
categorie_data = json['categories']
catlist = json['sub']
print(categorie_data)
with open('catlist.txt','w',encoding='utf-8') as f:
    for item in categorie_data:
        f.write(categorie_data[item] + ' ')
    f.write('\n')
    for i in range(len(catlist)):
        f.write(str(i) + ' ' + catlist[i]['name'] + '\n')
