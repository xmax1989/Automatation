import allure
import requests


class company:

    def __init__(self, url):
        self.url = url

    @allure.step("api получить токен авторизации {user}:{password}")
    def get_token(self, user='flora', password='nature-fairy'):
        creds = {
            'username': user,
            'password': password
        }
        resp = requests.post(self.url+'/auth/login', json=creds)
        return resp.json()["userToken"]

    @allure.step("api создаем новую компанию name={name} {description}")
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

    @allure.step("api получаем инфо о компании по id={id}")
    def get_company(self, id):
        resp = requests.get(self.url+'/company/' + str(id))
        return resp.json()
