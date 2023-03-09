import requests

from pprint import pprint

token = ''
upload_link = 'https://cloud-api.yandex.net/v1/disk/resources/upload'

home_link = input()
#C:\Users\Алексей\Desktop\777.txt

with open(home_link, 'r+', encoding='utf-8') as file:
    a = file.read()

headers = {
    "Content - Type":"application/json",
    "Authorization": f"OAuth {token}" }

def get_link_upload(url):
    params = { 'path':'test.txt', 'overwrite': 'true'}
    upload_link_ = requests.get(url, headers=headers, params=params)
    pprint(upload_link_.status_code)
    return upload_link_.json()['href']

def upload_file(url):
    res = get_link_upload(upload_link)
    upload_file = requests.put(res, data=open('text.txt', 'rb'))

if __name__ == '__main__':
    with open('text.txt', 'w+', encoding='utf-8') as f:
        f.write(a)
    upload_file(get_link_upload(upload_link))

