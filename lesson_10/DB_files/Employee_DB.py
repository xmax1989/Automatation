import allure
from sqlalchemy import create_engine
from sqlalchemy import text


class employeeDB:

    def __init__(self, connection_string):
        self.db = create_engine(connection_string)

    @allure.step("DB удаление сотрудника из б.д.по id:{id}")
    def delete_employee(self, id):
        sql = text('delete from employee where id = :id_delete')
        self.db.execute(sql, id_delete=id)
        allure.attach(str(sql.text), 'SQL', allure.attachment_type.TEXT)

    @allure.step("DB получение сотрудника из б.д.по id компании:{id}")
    def get_max_employee_id(self, id):
        sql = text('select MAX(id) from employee where company_id = :c_id')
        result = self.db.execute(sql, c_id=id)
        allure.attach(str(sql.text), 'SQL', allure.attachment_type.TEXT)
        return result.fetchall()[0][0]

    @allure.step("DB создание сотрудника в б.д.по id компании:{company_id}\
            {first_name} {last_name} {phone}")
    def create_employee(self, company_id: int, first_name: str,
                        last_name: str, phone: str):
        sql = text(
            'insert into employee(company_id, first_name, last_name, phone)\
                values(:id, :name, :surname, :phone)'
            )
        result = self.db.execute(sql, id=company_id, name=first_name,
                                 surname=last_name, phone=phone)
        allure.attach(str(sql.text), 'SQL', allure.attachment_type.TEXT)
        return result

    @allure.step("DB cписок сотрудников компании в б.д.по id компании:{company_id}")
    def employee_list(self, company_id):
        sql = text('select * from employee where company_id = :id')
        result = self.db.execute(sql, id=company_id)
        allure.attach(str(sql.text), 'SQL', allure.attachment_type.TEXT)
        return result

    @allure.step("DB редактирование сотрудника в б.д.по id сотрудника:{id} {first_name}")
    def employee_Update(self, first_name, id):
        sql = text(
            'update employee set first_name = :new_name where id = :employer_id'
            )
        result = self.db.execute(sql, new_name=first_name, employer_id=id)
        allure.attach(str(sql.text), 'SQL', allure.attachment_type.TEXT)
        return result
