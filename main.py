import requests
from pprint import pprint

TOKEN = ''

home_link = input()
# # home_link: C:\Users\Алексей\Desktop\777.txt
with open(home_link, 'r+', encoding='utf_8') as file:
    f = file.read()

class YaUploader:
    def __init__(self, token):
        self.token = token

    def headers(self):
        return  {
    "Content - Type":"application/json",
    "Authorization": f"OAuth {self.token}" }

    def _get_upload_link(self, file_path):
        upload_link = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        params = {'path':file_path, 'overwrite':'true'}
        up_link = requests.get(upload_link, headers=self.headers(), params=params)
        return up_link.json()['href']

    def upload_file(self, file_path, file_name):
        up_file = requests.put(self._get_upload_link(file_path), data=open(file_name,'rb'))
        if up_file.status_code == 201:
            print('Готово!')

if __name__ == '__main__':
    some_link = YaUploader(TOKEN)
    with open('test.txt', 'w+', encoding='UTF-8') as file:
        res = file.write(f)
    some_link.upload_file('test.txt','test.txt')


