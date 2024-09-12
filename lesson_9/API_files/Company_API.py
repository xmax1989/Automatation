import requests


class company:

    def __init__(self, url):
        self.url = url

    # авторизация
    def get_token(self, user='flora', password='nature-fairy'):
        creds = {
            'username': user,
            'password': password
        }
        resp = requests.post(self.url+'/auth/login', json=creds)
        return resp.json()["userToken"]

    # создаем новую компанию
    def create_company(self, name='Noname', description=''):
        company = {
            'name': name,
            'description': description
        }
        my_headers = {}
        my_headers["x-client-token"] = self.get_token()
        resp = requests.post(self.url+'/company',
                             json=company, headers=my_headers)
        return resp.json()

    # инфо о компании по id
    def get_company(self, id):
        resp = requests.get(self.url+'/company/' + str(id))
        return resp.json()
