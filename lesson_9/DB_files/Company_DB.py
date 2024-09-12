from sqlalchemy import create_engine
from sqlalchemy import text


class companyDB:
    def __init__(self, connection_string):
        self.db = create_engine(connection_string)

    # создание компании в б.д.
    def create_company(self, name):
        sql = text("insert into company(\"name\") values (:new_name)")
        result = self.db.execute(sql, new_name=name)
        return result

    # макс id компании в б.д.
    def get_max_company_id(self):
        sql = text('select MAX(id) from company')
        return self.db.execute(sql).fetchall()[0][0]

    # удаление компании из б.д.
    def delete_company(self, id):
        sql = text("delete from company where id = :id_to_delete")
        self.db.execute(sql, id_to_delete=id)
