import allure
import requests


class clients:

    def __init__(self, url):
        self.url = url

    @allure.step("api получить токен авторизации {user}:{password}")
    def get_token(self, user='bloom', password='fire-fairy'):
        creds = {
            'username': user,
            'password': password
        }
        resp = requests.post(self.url+'/auth/login', json=creds)
        return resp.json()["userToken"]

    @allure.step("api создаем нового сотрудника для компании \
                {firname} {laname} {MIDname} {CompID} \
                {EMAIL} {URL} {PHONE} {BIRdate}")
    def post_employee(self, firname="string", laname="string",
                      MIDname="string", CompID=0, EMAIL="string",
                      URL="string", PHONE="string",
                      BIRdate="2024-09-05T06:11:32.856Z"):
        client = {
            "id": 0,
            "firstName": firname,
            "lastName": laname,
            "middleName": MIDname,
            "companyId": CompID,
            "email": EMAIL,
            "url": URL,
            "phone": PHONE,
            "birthdate": BIRdate,
            "isActive": True
        }
        my_headers = {}
        my_headers["x-client-token"] = self.get_token()
        resp = requests.post(self.url+'/employee',
                             json=client, headers=my_headers)
        return resp.json()

    @allure.step("api получаем инфо о сотруднике по id компании:{id}")
    def get_employee_company_list(self, id):
        resp = requests.get(self.url+'/employee?company=' + str(id))
        return resp.json()

    @allure.step("получаем инфо о сотруднике по id сотрудника:{id}")
    def get_employee_ID(self, id):
        resp = requests.get(self.url+'/employee/' + str(id))
        return resp.json()

    @allure.step("api редактируем сотрудника по id:{id} {firname} \
                {laname} {MIDname} {CompID} {EMAIL} \
                {URL} {PHONE} {BIRdate} {ISACT}")
    def patch_employee_id(self, id, firname="string", laname="string",
                          MIDname="string", CompID=0, EMAIL="string",
                          URL="string", PHONE="string",
                          BIRdate="2024-09-05T06:11:32.856Z", ISACT=True):
        client = {
            "id": 0,
            "firstName": firname,
            "lastName": laname,
            "middleName": MIDname,
            "companyId": CompID,
            "email": EMAIL,
            "url": URL,
            "phone": PHONE,
            "birthdate": BIRdate,
            "isActive": ISACT
        }
        my_headers = {}
        my_headers["x-client-token"] = self.get_token()
        resp = requests.patch(self.url+'/employee/' +
                              str(id), json=client, headers=my_headers)
        return resp.json()
