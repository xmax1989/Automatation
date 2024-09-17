import allure
from sqlalchemy import create_engine
from sqlalchemy import text


class companyDB:
    def __init__(self, connection_string):
        self.db = create_engine(connection_string)

    @allure.step("DB создание компании в б.д. name:{name}")
    def create_company(self, name):
        sql = text("insert into company(\"name\") values (:new_name)")
        result = self.db.execute(sql, new_name=name)
        allure.attach(str(sql.text), 'SQL', allure.attachment_type.TEXT)
        return result

    @allure.step("DB получение макс id компании в б.д.")
    def get_max_company_id(self):
        sql = text('select MAX(id) from company')
        result = self.db.execute(sql)
        allure.attach(str(sql.text), 'SQL', allure.attachment_type.TEXT)
        return result.fetchall()[0][0]

    @allure.step("DB удаление компании из б.д. по id:{id}")
    def delete_company(self, id):
        sql = text("delete from company where id = :id_to_delete")
        self.db.execute(sql, id_to_delete=id)
        allure.attach(str(sql.text), 'SQL', allure.attachment_type.TEXT)
