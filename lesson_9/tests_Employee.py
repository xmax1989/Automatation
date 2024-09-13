import pytest
from API_files.Clients_API import clients
from API_files.Company_API import company
from DB_files.Employee_DB import employeeDB
from DB_files.Company_DB import companyDB

api = clients("https://x-clients-be.onrender.com")
apiComp = company("https://x-clients-be.onrender.com")
dbEMPL = employeeDB("postgresql+psycopg2://x_clients_user:ypYaT7FBULZv2VxrJuOHVoe78MEElWlb@dpg-crgp14o8fa8c73aritj0-a.frankfurt-postgres.render.com/x_clients_db_75hr")
dbComp = companyDB("postgresql+psycopg2://x_clients_user:ypYaT7FBULZv2VxrJuOHVoe78MEElWlb@dpg-crgp14o8fa8c73aritj0-a.frankfurt-postgres.render.com/x_clients_db_75hr")


@pytest.mark.test_positive
def test_create_employeeBD_pass():
    # создаем новую компанию в б.д.
    name = 'NewCompany'
    dbComp.create_company(name)

    # получаем id созданной компании
    newComp_id = dbComp.get_max_company_id()

    # создаем и добавляем нового сотрудника в б.д.
    FnameS = 'Nikolai'
    lasName = 'Nikolaev'
    companyId = newComp_id
    phone = 'string'
    dbEMPL.create_employee(company_id=companyId, first_name=FnameS,
                           last_name=lasName, phone=phone)

    # получаем сотрудника по id компании из б.д.
    sotr_id = dbEMPL.get_max_employee_id(newComp_id)

    # удалем сотрудника из б.д.
    dbEMPL.delete_employee(sotr_id)
    # удалем компанию из б.д.
    dbComp.delete_company(newComp_id)


@pytest.mark.test_positive
def test_get_max_id_employeeBD_pass():
    # создаем новую компанию в б.д.
    name = 'NewCompany'
    dbComp.create_company(name)

    # получаем id созданной компании
    newComp_id = dbComp.get_max_company_id()

    # создаем и добавляем нового сотрудника в б.д.
    FnameS = 'Nikolai'
    lasName = 'Nikolaev'
    companyId = newComp_id
    phone = 'string'
    dbEMPL.create_employee(company_id=companyId, first_name=FnameS,
                           last_name=lasName, phone=phone)

    # получаем инфо о сотруднике по id из б.д.
    sotr_id = dbEMPL.get_max_employee_id(newComp_id)

    # дергаем апи проверяем добавленного сотрудника по id из б.д.
    body = api.get_employee_ID(sotr_id)
    assert body["firstName"] == FnameS    # проверяем имя
    assert body["lastName"] == lasName    # проверяем фамилию
    assert body["id"] == sotr_id          # проверяем ID сотрудника

    # удалем сотрудника из б.д.
    dbEMPL.delete_employee(sotr_id)
    # удалем компанию из б.д.
    dbComp.delete_company(newComp_id)


@pytest.mark.test_positive
def test_update_employeeBD_pass():
    # создаем новую компанию в б.д.
    name = 'NewCompany'
    dbComp.create_company(name)

    # получаем id созданной компании
    newComp_id = dbComp.get_max_company_id()

    # создаем и добавляем нового сотрудника в б.д.
    FnameS = 'Nikolai'
    lasName = 'Nikolaev'
    companyId = newComp_id
    phone = 'string'
    dbEMPL.create_employee(company_id=companyId, first_name=FnameS,
                           last_name=lasName, phone=phone)

    # получаем инфо о сотруднике по id из б.д.
    sotr_id = dbEMPL.get_max_employee_id(newComp_id)

    # дергаем апи проверяем добавленного сотрудника по id из б.д.
    body = api.get_employee_ID(sotr_id)
    assert body["firstName"] == FnameS  # проверяем имя созданного сотрудника

    # редактируем нового сотрудника
    RenameS = 'Sergey'                   # меняем имя созданного сотрудника

    dbEMPL.employee_Update(first_name=RenameS, id=sotr_id)

    # получаем инфо о сотруднике по id из б.д.
    sotr_id = dbEMPL.get_max_employee_id(newComp_id)

    # дергаем апи проверяем сотрудника по id из б.д. после редактирования
    body = api.get_employee_ID(sotr_id)
    assert body["firstName"] == RenameS  # проверяем имя созданного сотрудника

    # удалем сотрудника из б.д.
    dbEMPL.delete_employee(sotr_id)
    # удалем компанию из б.д.
    dbComp.delete_company(newComp_id)


@pytest.mark.test_negative  # пустое поле имя (проходит с пустым полем)
@pytest.mark.xfail
def test_create_employee_fail():
    # создаем новую компанию в б.д.
    name = 'NewCompany'
    dbComp.create_company(name)

    # получаем id созданной компании
    newComp_id = dbComp.get_max_company_id()

    # создаем и добавляем нового сотрудника в б.д.
    FnameS = ''
    lasName = 'Nikolaev'
    companyId = newComp_id
    phone = 'string'
    dbEMPL.create_employee(company_id=companyId, first_name=FnameS,
                           last_name=lasName, phone=phone)

    # получаем сотрудника по id компании из б.д.
    sotr_id = dbEMPL.get_max_employee_id(newComp_id)

    # удалем сотрудника из б.д.
    dbEMPL.delete_employee(sotr_id)
    # удалем компанию из б.д.
    dbComp.delete_company(newComp_id)


@pytest.mark.test_negative  # пустое поле фамилия (проходит с пустым полем)
@pytest.mark.xfail
def test_create_employee_fail1():
    # создаем новую компанию в б.д.
    name = 'NewCompany'
    dbComp.create_company(name)

    # получаем id созданной компании
    newComp_id = dbComp.get_max_company_id()

    # создаем и добавляем нового сотрудника в б.д.
    FnameS = 'Nikolai'
    lasName = ''
    companyId = newComp_id
    phone = 'string'
    dbEMPL.create_employee(company_id=companyId, first_name=FnameS,
                           last_name=lasName, phone=phone)

    # получаем сотрудника по id компании из б.д.
    sotr_id = dbEMPL.get_max_employee_id(newComp_id)

    # удалем сотрудника из б.д.
    dbEMPL.delete_employee(sotr_id)
    # удалем компанию из б.д.
    dbComp.delete_company(newComp_id)


@pytest.mark.test_negative  # пустое поле телефон (проходит с пустым полем)
@pytest.mark.xfail
def test_create_employee_fail2():
    # создаем новую компанию в б.д.
    name = 'NewCompany'
    dbComp.create_company(name)

    # получаем id созданной компании
    newComp_id = dbComp.get_max_company_id()

    # создаем и добавляем нового сотрудника в б.д.
    FnameS = 'Nikolai'
    lasName = 'Nikolaev'
    companyId = newComp_id
    phone = ''
    dbEMPL.create_employee(company_id=companyId, first_name=FnameS,
                           last_name=lasName, phone=phone)

    # получаем сотрудника по id компании из б.д.
    sotr_id = dbEMPL.get_max_employee_id(newComp_id)

    # удалем сотрудника из б.д.
    dbEMPL.delete_employee(sotr_id)
    # удалем компанию из б.д.
    dbComp.delete_company(newComp_id)


@pytest.mark.test_negative  # все поля пустые(тест проходит)
@pytest.mark.xfail
def test_create_employee_fail3():
    # создаем новую компанию в б.д.
    name = 'NewCompany'
    dbComp.create_company(name)

    # получаем id созданной компании
    newComp_id = dbComp.get_max_company_id()

    # создаем и добавляем нового сотрудника в б.д.
    FnameS = ''
    lasName = ''
    companyId = newComp_id
    phone = ''
    dbEMPL.create_employee(company_id=companyId, first_name=FnameS,
                           last_name=lasName, phone=phone)

    # получаем сотрудника по id компании из б.д.
    sotr_id = dbEMPL.get_max_employee_id(newComp_id)

    # удалем сотрудника из б.д.
    dbEMPL.delete_employee(sotr_id)
    # удалем компанию из б.д.
    dbComp.delete_company(newComp_id)
