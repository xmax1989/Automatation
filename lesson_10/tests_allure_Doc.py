import allure
import pytest
from API_files.Clients_API import clients
from API_files.Company_API import company
from DB_files.Employee_DB import employeeDB
from DB_files.Company_DB import companyDB

api = clients("https://x-clients-be.onrender.com")
apiComp = company("https://x-clients-be.onrender.com")
dbEMPL = employeeDB("postgresql+psycopg2://x_clients_user:ypYaT7FBULZv2VxrJuOHVoe78MEElWlb@dpg-crgp14o8fa8c73aritj0-a.frankfurt-postgres.render.com/x_clients_db_75hr")
dbComp = companyDB("postgresql+psycopg2://x_clients_user:ypYaT7FBULZv2VxrJuOHVoe78MEElWlb@dpg-crgp14o8fa8c73aritj0-a.frankfurt-postgres.render.com/x_clients_db_75hr")


@allure.epic("сотрудники EMPLOYEE")
@allure.title("создание нового сотрудника")
@allure.severity("bloker")
@allure.id("Test-1")
@pytest.mark.test_positive
def test_create_employeeBD_pass():
    name = 'NewCompany'
    dbComp.create_company(name)
    newComp_id = dbComp.get_max_company_id()
    FnameS = 'Nikolai'
    lasName = 'Nikolaev'
    companyId = newComp_id
    phone = 'string'
    dbEMPL.create_employee(company_id=companyId, first_name=FnameS,
                           last_name=lasName, phone=phone)
    sotr_id = dbEMPL.get_max_employee_id(newComp_id)

    with allure.step("удаляем тестовые данные"):
        dbEMPL.delete_employee(sotr_id)
        dbComp.delete_company(newComp_id)


@allure.epic("сотрудники EMPLOYEE")
@allure.title("проверяем создание нового сотрудника")
@allure.severity("bloker")
@allure.id("Test-2")
@pytest.mark.test_positive
def test_get_max_id_employeeBD_pass():
    name = 'NewCompany'
    dbComp.create_company(name)
    newComp_id = dbComp.get_max_company_id()
    FnameS = 'Nikolai'
    lasName = 'Nikolaev'
    companyId = newComp_id
    phone = 'string'
    dbEMPL.create_employee(company_id=companyId, first_name=FnameS,
                           last_name=lasName, phone=phone)

    sotr_id = dbEMPL.get_max_employee_id(newComp_id)
    with allure.step("api проверяем добавленного сотрудника по id из б.д."):
        body = api.get_employee_ID(sotr_id)
        with allure.step("проверяем имя"):
            assert body["firstName"] == FnameS
        with allure.step("проверяем фамилию"):
            assert body["lastName"] == lasName
        with allure.step("проверяем ID сотрудника"):
            assert body["id"] == sotr_id

    with allure.step("удаляем тестовые данные"):
        dbEMPL.delete_employee(sotr_id)
        dbComp.delete_company(newComp_id)


@allure.epic("сотрудники EMPLOYEE")
@allure.title("редактируем нового сотрудника по ID")
@allure.severity("high")
@allure.id("Test-3")
@pytest.mark.test_positive
def test_update_employeeBD_pass():
    name = 'NewCompany'
    dbComp.create_company(name)
    newComp_id = dbComp.get_max_company_id()
    FnameS = 'Nikolai'
    lasName = 'Nikolaev'
    companyId = newComp_id
    phone = 'string'
    dbEMPL.create_employee(company_id=companyId, first_name=FnameS,
                           last_name=lasName, phone=phone)
    sotr_id = dbEMPL.get_max_employee_id(newComp_id)
    with allure.step("api проверяем добавленного сотрудника по id из б.д."):
        body = api.get_employee_ID(sotr_id)
        with allure.step("проверяем имя созданного сотрудника"):
            assert body["firstName"] == FnameS

    RenameS = 'Sergey'
    dbEMPL.employee_Update(first_name=RenameS, id=sotr_id)
    sotr_id = dbEMPL.get_max_employee_id(newComp_id)
    with allure.step("api проверяем сотрудника после редактирования"):
        body = api.get_employee_ID(sotr_id)
        with allure.step("проверяем имя созданного сотрудника"):
            assert body["firstName"] == RenameS

    with allure.step("удаляем тестовые данные"):
        dbEMPL.delete_employee(sotr_id)
        dbComp.delete_company(newComp_id)


@allure.epic("сотрудники EMPLOYEE")
@allure.title("негативный тест создание нового сотрудника")
@allure.description("пустое поле имя (проходит с пустым полем)")
@allure.severity("low")
@allure.id("Test-4")
@pytest.mark.test_negative
@pytest.mark.xfail
def test_create_employee_fail():
    name = 'NewCompany'
    dbComp.create_company(name)
    newComp_id = dbComp.get_max_company_id()
    FnameS = ''
    lasName = 'Nikolaev'
    companyId = newComp_id
    phone = 'string'
    dbEMPL.create_employee(company_id=companyId, first_name=FnameS,
                           last_name=lasName, phone=phone)
    sotr_id = dbEMPL.get_max_employee_id(newComp_id)

    with allure.step("удаляем тестовые данные"):
        dbEMPL.delete_employee(sotr_id)
        dbComp.delete_company(newComp_id)


@allure.epic("сотрудники EMPLOYEE")
@allure.title("негативный тест создание нового сотрудника")
@allure.description("пустое поле фамилия (проходит с пустым полем)")
@allure.severity("low")
@allure.id("Test-5")
@pytest.mark.test_negative
@pytest.mark.xfail
def test_create_employee_fail1():
    name = 'NewCompany'
    dbComp.create_company(name)
    newComp_id = dbComp.get_max_company_id()
    FnameS = 'Nikolai'
    lasName = ''
    companyId = newComp_id
    phone = 'string'
    dbEMPL.create_employee(company_id=companyId, first_name=FnameS,
                           last_name=lasName, phone=phone)
    sotr_id = dbEMPL.get_max_employee_id(newComp_id)

    with allure.step("удаляем тестовые данные"):
        dbEMPL.delete_employee(sotr_id)
        dbComp.delete_company(newComp_id)


@allure.epic("сотрудники EMPLOYEE")
@allure.title("негативный тест создание нового сотрудника")
@allure.description("пустое поле телефон (проходит с пустым полем)")
@allure.severity("low")
@allure.id("Test-6")
@pytest.mark.test_negative
@pytest.mark.xfail
def test_create_employee_fail2():
    name = 'NewCompany'
    dbComp.create_company(name)
    newComp_id = dbComp.get_max_company_id()
    FnameS = 'Nikolai'
    lasName = 'Nikolaev'
    companyId = newComp_id
    phone = ''
    dbEMPL.create_employee(company_id=companyId, first_name=FnameS,
                           last_name=lasName, phone=phone)
    sotr_id = dbEMPL.get_max_employee_id(newComp_id)

    with allure.step("удаляем тестовые данные"):
        dbEMPL.delete_employee(sotr_id)
        dbComp.delete_company(newComp_id)


@allure.epic("сотрудники EMPLOYEE")
@allure.title("негативный тест создание нового сотрудника")
@allure.description("все поля пустые(тест проходит)")
@allure.severity("low")
@allure.id("Test-7")
@pytest.mark.test_negative
@pytest.mark.xfail
def test_create_employee_fail3():
    name = 'NewCompany'
    dbComp.create_company(name)
    newComp_id = dbComp.get_max_company_id()
    FnameS = ''
    lasName = ''
    companyId = newComp_id
    phone = ''
    dbEMPL.create_employee(company_id=companyId, first_name=FnameS,
                           last_name=lasName, phone=phone)
    sotr_id = dbEMPL.get_max_employee_id(newComp_id)

    with allure.step("удаляем тестовые данные"):
        dbEMPL.delete_employee(sotr_id)
        dbComp.delete_company(newComp_id)


@allure.epic("сотрудники EMPLOYEE")
@allure.title("Сломанный тест")
@allure.description("Тест сломан добавлен для отчета")
@allure.id("Test-8")
@pytest.mark.test_negative
def test_get_max_id_employeeBDfail4():
    name = 'NewCompany'
    dbComp.create_company(name)
    newComp_id = dbComp.get_max_company_id()
    FnameS = 'Nikolai'
    lasName = 'Nikolaev'
    companyId = newComp_id
    phone = 'string'
    dbEMPL.create_employee(company_id=companyId, first_name=FnameS,
                           last_name=lasName, phone=phone)

    sotr_id = dbEMPL.get_max_employee_id(newComp_id)
    with allure.step("api проверяем добавленного сотрудника по id из б.д."):
        body = api.get_employee_ID(sotr_id)
        with allure.step("проверяем имя"):
            try:
                assert body["firstName"] == FnameS+"1"
            finally:
                with allure.step("удаляем тестовые данные"):
                    dbEMPL.delete_employee(sotr_id)
                    dbComp.delete_company(newComp_id)
