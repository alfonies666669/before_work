import requests
from config import *

HEADER = {"Authorization": key}


def get_attr(what: str):
    id_pic = ''
    url = f"https://api.pexels.com/v1/search?query={what}&per_page=1"
    resp = requests.get(url, headers=HEADER)
    if resp.status_code == 200:
        _r = resp.json()
        for i in _r.get("photos"):
            id_pic = i.get('id')
            download_pic(id_pic, what)
    else:
        print(resp.status_code)


def get_what():
    print("What do you want?")
    what = input()
    get_attr(what)


def download_pic(id_pic, what):

    url_img = f"https://api.pexels.com/v1/photos/{id_pic}"
    p = requests.get(url_img, headers=HEADER)
    if p.status_code == 200:
        _p = p.json()
        src = _p.get('src')
        url_image = src.get("original")
        p = requests.get(url_image)
        out = open(rf"C:\Users\Serafim\Desktop\{what}.jpg", "wb")
        out.write(p.content)
        out.close()
    else:
        print(p.status_code)


get_what()
