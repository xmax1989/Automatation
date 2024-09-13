from sqlalchemy import create_engine
from sqlalchemy import text


class employeeDB:

    def __init__(self, connection_string):
        self.db = create_engine(connection_string)

    # удаление сотрудника из б.д.
    def delete_employee(self, id):
        sql = text('delete from employee where id = :id_delete')
        self.db.execute(sql, id_delete=id)

    # получение сотрудника из б.д. по id компании
    def get_max_employee_id(self, id):
        sql = text('select MAX(id) from employee where company_id = :c_id')
        result = self.db.execute(sql, c_id=id).fetchall()[0][0]
        return result

    # создание сотрудника в б.д.
    def create_employee(self, company_id: int, first_name: str,
                        last_name: str, phone: str):
        sql = text(
            'insert into employee(company_id, first_name, last_name, phone) values(:id, :name, :surname, :phone)'
            )
        result = self.db.execute(sql, id=company_id, name=first_name,
                                 surname=last_name, phone=phone)
        return result

    # cписок сотрудников компании в б.д.
    def employee_list(self, company_id):
        sql = text('select * from employee where company_id = :id')
        result = self.db.execute(sql, id=company_id)
        return result

    # редактирование сотрудника в б.д.
    def employee_Update(self, first_name, id):
        sql = text(
            'update employee set first_name = :new_name where id = :employer_id'
            )
        result = self.db.execute(sql, new_name=first_name, employer_id=id)
        return result
