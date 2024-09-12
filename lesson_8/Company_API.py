import requests


class company:

    def __init__(self, url):
        self.url = url
    
    def get_token(self, user='bloom', password='fire-fairy'): # авторизация
        creds = {
            'username': user,
            'password': password
        }
        resp = requests.post(self.url+'/auth/login', json=creds)
        return resp.json()["userToken"]
    
        
    def create_company(self,name='Noname', description=''):
        company = {
            'name': name,
            'description': description
        }   
        my_headers = {}
        my_headers["x-client-token"] = self.get_token()  # создаем новую компанию
        resp = requests.post(self.url+'/company', json=company, headers=my_headers)
        return resp.json()