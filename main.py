import requests
import json
import TOKEN

# class Yandex:
#
#     base_host = 'https://cloud-api.yandex.net/'
#
#
#     def __init__(self, token):
#         self.token = token
#
#     def get_headers(self):
#         return {
#             'Content-Type': 'application/json',
#             'Authorization': f'OAuth {self.token}'
#         }
#
#     def get_file_list(self):
#         uri = 'v1/disk/resources/files/'
#         requests_url = self.base_host + uri
#         params = {'limit': 2}
#         response = requests.get(requests_url, headers=self.get_headers(), params=params)
#         print(response.json())
#
#     def _get_upload_link(self, path):
#         uri = 'v1/disk/resources/upload/'
#         request_url = self.base_host + uri
#         params = {'path': path, 'overwrite': True}
#         response = requests.get(request_url, headers=self.get_headers(), params=params)
#         print(response.json())
#         return response.json()['href']
#
#     def upload_to_disk(self, local_path, yandex_path):
#         upload_url = self._get_upload_link(yandex_path)
#         response = requests.put(upload_url, data=open(local_path, 'rb'), headers=self.get_headers())
#         if response.status_code == 201:
#             print('Загрузка произошла успешно!')
#
# if __name__ == '__main__':
#     ya = Yandex(TOKEN)
#     ya.upload_to_disk('C:/Users/Slava/Downloads/Telegram Desktop/5F284A4E-C680-4DB8-B457-F8566DC9914A.JPG', '/5F284A4E-C680-4DB8-B457-F8566DC9914A.JPG')
#     ya.get_file_list()




# Task 1



def hero(id):
    base_host = 'https://akabab.github.io/superhero-api/api'
    uri = '/powerstats/' + str(id) + '.json'
    url = base_host + uri
    response = requests.get(url)
    hero_specifications = response.text
    res = json.loads(hero_specifications)
    return res


hulk_intel = hero(332)['intelligence']
cap_intel = hero(149)['intelligence']
thanos_intel = hero(655)['intelligence']

hero_list = {'Hulk': hulk_intel, 'Captain_America': cap_intel, 'Thanos': thanos_intel}
smartest_hero = max(hero_list, key=hero_list.get)


print(f'Самый умный {smartest_hero}')



#Task 2


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        """Метод загружает файлы по списку file_list на яндекс диск"""
        # Тут ваша логика
        # Функция может ничего не возвращать


if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = ...
    token = ...
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)


    class Yandex:
        base_host = 'https://cloud-api.yandex.net/'


    def __init__(self, token):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }

    def get_file_list(self):
        uri = 'v1/disk/resources/files/'
        requests_url = self.base_host + uri
        params = {'limit': 2}
        response = requests.get(requests_url, headers=self.get_headers(), params=params)
        print(response.json())

    def _get_upload_link(self, path):
        uri = 'v1/disk/resources/upload/'
        request_url = self.base_host + uri
        params = {'path': path, 'overwrite': True}
        response = requests.get(request_url, headers=self.get_headers(), params=params)
        print(response.json())
        return response.json()['href']

    def upload_to_disk(self, local_path, yandex_path):
        upload_url = self._get_upload_link(yandex_path)
        response = requests.put(upload_url, data=open(local_path, 'rb'), headers=self.get_headers())
        if response.status_code == 201:
            print('Загрузка произошла успешно!')

if __name__ == '__main__':
    ya = Yandex(TOKEN)
    ya.upload_to_disk('hello_word.txt', '/hello.txt')
    # ya.get_file_list()


# # class YaUploader:
# #     def __init__(self, token: str):
# #         self.token = token
# #
# #     def upload(self, file_path: str):
# #         """Метод загружает файлы по списку file_list на яндекс диск"""
# #         # Тут ваша логика
# #         # Функция может ничего не возвращать
# #
# #
# # if __name__ == '__main__':
# #     # Получить путь к загружаемому файлу и токен от пользователя
# #     path_to_file = ...
# #     token = ...
# #     uploader = YaUploader(token)
# #     result = uploader.upload(path_to_file)