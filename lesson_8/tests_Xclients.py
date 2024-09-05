import pytest
from Clients_API import clients
from Company_API import company

api = clients("https://x-clients-be.onrender.com")
apiComp = company("https://x-clients-be.onrender.com")


@pytest.mark.test_positive
def test_add_employee_pass():
    # создаем новую компанию
    name = 'NEW CITY'
    descript = 'CITY NEW'
    new_company = apiComp.create_company(name=name, description=descript)
    new_id = new_company["id"]
    # создаем и добавляем нового сотрудника
    FnameS = 'Nikolai'
    lasName = 'Nikolaev'
    MidName = 'Nikolaevich'
    companyId = new_id
    Mail = 'string@mail.com'
    uRl = 'string'
    phone = 'string'
    birthdate = '2024-09-05T06:11:32.856Z'
    api.post_employee(firname=FnameS, laname=lasName, MIDname=MidName,
                      CompID=companyId, EMAIL=Mail)
    # проверяем создание и добавление сотрудника в список сотрудников в комании
    id = new_id
    resp = api.get_employee_company_list(id)
    assert resp[-1]["firstName"] == FnameS  # проверяем имя
    assert resp[-1]["lastName"] == lasName  # проверяем фамилию
    assert resp[-1]["companyId"] == new_id  # проверяем ID компании
    
@pytest.mark.test_positive
def test_get_employee_pass():
    # создаем новую компанию
    name = 'NEW CITY'
    descript = 'CITY NEW'
    new_company = apiComp.create_company(name=name, description=descript)
    new_id = new_company["id"]
    # создаем и добавляем нового сотрудника
    FnameS = 'Nikolai'
    lasName = 'Nikolaev'
    MidName = 'Nikolaevich'
    companyId = new_id
    Mail = 'string@mail.com'
    uRl = 'string'
    phone = 'string'
    birthdate = '2024-09-05T06:11:32.856Z'
    new_sotrudnik = api.post_employee(firname=FnameS, laname=lasName,
                                      MIDname=MidName, CompID=companyId, EMAIL=Mail)   
    # получаем инфо о сотруднике по id
    id = new_sotrudnik["id"]
    body = api.get_employee_ID(id)
    assert body["firstName"] == FnameS    # проверяем имя
    assert body["lastName"] == lasName    # проверяем фамилию
    assert body["middleName"] == MidName  # проверяем отчество
    assert body["id"] == id               # проверяем ID сотрудника
    
@pytest.mark.test_positive
def test_patch_employee_pass():
    # создаем новую компанию
    name = 'NEW CITY'
    descript = 'CITY NEW'
    new_company = apiComp.create_company(name=name, description=descript)
    new_id = new_company["id"]
    # создаем и добавляем нового сотрудника
    FnameS = 'Nikolai'
    lasName = 'Nikolaev'
    MidName = 'Nikolaevich'
    companyId = new_id
    Mail = 'string@mail.com'
    uRl = 'string'
    phone = 'string'
    birthdate = '2024-09-05T06:11:32.856Z'
    new_sotrudnik = api.post_employee(firname=FnameS, laname=lasName,
                                      MIDname=MidName, CompID=companyId, EMAIL=Mail)
    id = new_sotrudnik["id"]
    body = api.get_employee_ID(id)
    assert body["firstName"] == FnameS  # проверяем имя созданного сотрудника
    # редактируем нового сотрудника
    lasName = 'Sergeev'                 # меняем фамилию созданного сотрудника
    Mail = 'newstring@mail.com'         # меняем имэйл созданного сотрудника
    uRl = 'string'                      # меняем урл созданного сотрудника
    phone = 'string'                    # меняем телефон созданного сотрудника
    isActive = False                    # меняем активность созданного сотрудника
    client_redact = api.patch_employee_id(id, laname=lasName, EMAIL=Mail,
                                          URL=uRl, PHONE=phone, ISACT=isActive)
    # получаем инфо о сотруднике после редактирования по id
    id = client_redact["id"]
    body = api.get_employee_ID(id)
    assert body["lastName"] == lasName   # проверяем фамилию
    assert body["email"] == Mail         # проверяем имэйл
    assert body["isActive"] == isActive  # проверяем активность
    
@pytest.mark.test_negative  # пустое поле имя (не проходит с пустым полем)
@pytest.mark.xfail
def test_add_employee_fail1():
    # создаем новую компанию
    name = 'NEW CITY'
    descript = 'CITY NEW'
    new_company = apiComp.create_company(name=name, description=descript)
    new_id = new_company["id"]
    # создаем и добавляем нового сотрудника
    FnameS = ''
    lasName = 'Nikolaev'
    MidName = 'Nikolaevich'
    companyId = new_id
    Mail = 'string@mail.com'
    uRl = 'string'
    phone = 'string'
    birthdate = '2024-09-05T06:11:32.856Z'
    api.post_employee(firname=FnameS, laname=lasName, MIDname=MidName,
                      CompID=companyId, EMAIL=Mail)
    # проверяем создание и добавление сотрудника в компанию список сотрудников в комании
    id = new_id
    resp = api.get_employee_company_list(id)
    assert resp[-1]["firstName"] == FnameS  # проверяем имя
    assert resp[-1]["lastName"] == lasName  # проверяем фамилию
    assert resp[-1]["companyId"] == new_id  # проверяем ID компании
    
@pytest.mark.test_negative  # пустое поле фамилия (проходит с пустым полем)
@pytest.mark.xfail
def test_add_employee_fail2():
    # создаем новую компанию
    name = 'NEW CITY'
    descript = 'CITY NEW'
    new_company = apiComp.create_company(name=name, description=descript)
    new_id = new_company["id"]
    # создаем и добавляем нового сотрудника
    FnameS = 'Nikolaei'
    lasName = ''
    MidName = 'Nikolaevich'
    companyId = new_id
    Mail = 'string@mail.com'
    uRl = 'string'
    phone = 'string'
    birthdate = '2024-09-05T06:11:32.856Z'
    api.post_employee(firname=FnameS, laname=lasName, MIDname=MidName,
                      CompID=companyId, EMAIL=Mail)
    # проверяем создание и добавление сотрудника в компанию список сотрудников в комании
    id = new_id
    resp = api.get_employee_company_list(id)
    assert resp[-1]["firstName"] == FnameS  # проверяем имя
    assert resp[-1]["lastName"] == lasName  # проверяем фамилию
    assert resp[-1]["companyId"] == new_id  # проверяем ID компании
    
@pytest.mark.test_negative  # пустое поле отчество (проходит с пустым полем)
@pytest.mark.xfail
def test_add_employee_fail3():
    # создаем новую компанию
    name = 'NEW CITY'
    descript = 'CITY NEW'
    new_company = apiComp.create_company(name=name, description=descript)
    new_id = new_company["id"]
    # создаем и добавляем нового сотрудника
    FnameS = 'Nikolaei'
    lasName = 'Nikolaev'
    MidName = ''
    companyId = new_id
    Mail = 'string@mail.com'
    uRl = 'string'
    phone = 'string'
    birthdate = '2024-09-05T06:11:32.856Z'
    api.post_employee(firname=FnameS, laname=lasName, MIDname=MidName,
                      CompID=companyId, EMAIL=Mail)
    # проверяем создание и добавление сотрудника в компанию список сотрудников в комании
    id = new_id
    resp = api.get_employee_company_list(id)
    assert resp[-1]["firstName"] == FnameS  # проверяем имя
    assert resp[-1]["lastName"] == lasName  # проверяем фамилию
    assert resp[-1]["companyId"] == new_id  # проверяем ID компании
    
@pytest.mark.test_negative  # пустое поле  имэйл (не проходит с пустым полем)
@pytest.mark.xfail
def test_add_employee_fail4():
    # создаем новую компанию
    name = 'NEW CITY'
    descript = 'CITY NEW'
    new_company = apiComp.create_company(name=name, description=descript)
    new_id = new_company["id"]
    # создаем и добавляем нового сотрудника
    FnameS = 'Nikolaei'
    lasName = 'Nikolaev'
    MidName = 'Nikolaevich'
    companyId = new_id
    Mail = ''
    uRl = 'string'
    phone = 'string'
    birthdate = '2024-09-05T06:11:32.856Z'
    api.post_employee(firname=FnameS, laname=lasName, MIDname=MidName,
                      CompID=companyId, EMAIL=Mail)
    # проверяем создание и добавление сотрудника в компанию список сотрудников в комании
    id = new_id
    resp = api.get_employee_company_list(id)
    assert resp[-1]["firstName"] == FnameS  # проверяем имя
    assert resp[-1]["lastName"] == lasName  # проверяем фамилию
    assert resp[-1]["companyId"] == new_id  # проверяем ID компании
    
@pytest.mark.test_negative  # пустое поле  урл (проходит с пустым полем)
@pytest.mark.xfail
def test_add_employee_fail5():
    # создаем новую компанию
    name = 'NEW CITY'
    descript = 'CITY NEW'
    new_company = apiComp.create_company(name=name, description=descript)
    new_id = new_company["id"]
    # создаем и добавляем нового сотрудника
    FnameS = 'Nikolaei'
    lasName = 'Nikolaev'
    MidName = 'Nikolaevich'
    companyId = new_id
    Mail = 'string@mail.com'
    uRl = ''
    phone = 'string'
    birthdate = '2024-09-05T06:11:32.856Z'
    api.post_employee(firname=FnameS, laname=lasName, MIDname=MidName,
                      CompID=companyId, EMAIL=Mail,URL=uRl)
    # проверяем создание и добавление сотрудника в компанию список сотрудников в комании
    id = new_id
    resp = api.get_employee_company_list(id)
    assert resp[-1]["firstName"] == FnameS  # проверяем имя
    assert resp[-1]["lastName"] == lasName  # проверяем фамилию
    assert resp[-1]["companyId"] == new_id  # проверяем ID компании
    
@pytest.mark.test_negative  # пустое поле  телефон (проходит с пустым полем)
@pytest.mark.xfail
def test_add_employee_fail6():
    # создаем новую компанию
    name = 'NEW CITY'
    descript = 'CITY NEW'
    new_company = apiComp.create_company(name=name, description=descript)
    new_id = new_company["id"]
    # создаем и добавляем нового сотрудника
    FnameS = 'Nikolaei'
    lasName = 'Nikolaev'
    MidName = 'Nikolaevich'
    companyId = new_id
    Mail = 'string@mail.com'
    uRl = 'string'
    phone = ''
    birthdate = '2024-09-05T06:11:32.856Z'
    api.post_employee(firname=FnameS, laname=lasName, MIDname=MidName,
                      CompID=companyId, EMAIL=Mail, URL=uRl, PHONE=phone)    
    # проверяем создание и добавление сотрудника в компанию список сотрудников в комании
    id = new_id
    resp = api.get_employee_company_list(id)
    assert resp[-1]["firstName"] == FnameS  # проверяем имя
    assert resp[-1]["lastName"] == lasName  # проверяем фамилию
    assert resp[-1]["companyId"] == new_id  # проверяем ID компании
    
@pytest.mark.test_negative  # пустое поле  дата рождения (не проходит с пустым полем)
@pytest.mark.xfail
def test_add_employee_fail7():
    # создаем новую компанию
    name = 'NEW CITY'
    descript = 'CITY NEW'
    new_company = apiComp.create_company(name=name, description=descript)
    new_id = new_company["id"]
    # создаем и добавляем нового сотрудника
    FnameS = 'Nikolaei'
    lasName = 'Nikolaev'
    MidName = 'Nikolaevich'
    companyId = new_id
    Mail = 'string@mail.com'
    uRl = 'string'
    phone = 'string'
    birthdate = ''
    api.post_employee(firname=FnameS, laname=lasName, MIDname=MidName,
                      CompID=companyId, EMAIL=Mail, URL=uRl, PHONE=phone, BIRdate=birthdate)     
    # проверяем создание и добавление сотрудника в компанию список сотрудников в комании
    id = new_id
    resp = api.get_employee_company_list(id)
    assert resp[-1]["firstName"] == FnameS  # проверяем имя
    assert resp[-1]["lastName"] == lasName  # проверяем фамилию
    assert resp[-1]["companyId"] == new_id  # проверяем ID компании
    
@pytest.mark.test_negative  # все поля пустые (не проходит с пустыми полями)
@pytest.mark.xfail
def test_add_employee_fail8():
    # создаем новую компанию
    name = 'NEW CITY'
    descript = 'CITY NEW'
    new_company = apiComp.create_company(name=name, description=descript)
    new_id = new_company["id"]
    # создаем и добавляем нового сотрудника
    FnameS = ''
    lasName = ''
    MidName = ''
    companyId = new_id
    Mail = ''
    uRl = ''
    phone = ''
    birthdate = ''
    api.post_employee(firname=FnameS, laname=lasName, MIDname=MidName,
                      CompID=companyId, EMAIL=Mail, URL=uRl, PHONE=phone, BIRdate=birthdate)   
    # проверяем создание и добавление сотрудника в компанию список сотрудников в комании
    id = new_id
    resp = api.get_employee_company_list(id)
    assert resp[-1]["firstName"] == FnameS   # проверяем имя
    assert resp[-1]["lastName"] == lasName   # проверяем фамилию
    assert resp[-1]["companyId"] == new_id   # проверяем ID компании
    
@pytest.mark.test_negative  # пустое поле id сотрудника(не проходит без id)
@pytest.mark.xfail
def test_get_employee_fail():
    # создаем новую компанию
    name = 'NEW CITY'
    descript = 'CITY NEW'
    new_company = apiComp.create_company(name=name, description=descript)
    new_id = new_company["id"]
    # создаем и добавляем нового сотрудника
    FnameS = 'Nikolai'
    lasName = 'Nikolaev'
    MidName = 'Nikolaevich'
    companyId = new_id
    Mail = 'string@mail.com'
    uRl = 'string'
    phone = 'string'
    birthdate = '2024-09-05T06:11:32.856Z'
    new_sotrudnik = api.post_employee(firname=FnameS, laname=lasName,
                                      MIDname=MidName, CompID=companyId, EMAIL=Mail)  
    # получаем инфо о сотруднике по id
    id = new_sotrudnik["id"]
    body = api.get_employee_ID()
    assert body["firstName"] == FnameS     # проверяем имя
    assert body["lastName"] == lasName     # проверяем фамилию
    assert body["middleName"] == MidName   # проверяем отчество
    assert body["id"] == id                # проверяем ID сотрудника
    
@pytest.mark.test_negative  # пустое поле id сотрудника(проходит без id)
@pytest.mark.xfail
def test_patch_employee_fail():
    # создаем новую компанию
    name = 'NEW CITY'
    descript = 'CITY NEW'
    new_company = apiComp.create_company(name=name, description=descript)
    new_id = new_company["id"]
    # создаем и добавляем нового сотрудника
    FnameS = 'Nikolai'
    lasName = 'Nikolaev'
    MidName = 'Nikolaevich'
    companyId = new_id
    Mail = 'string@mail.com'
    uRl = 'string'
    phone = 'string'
    birthdate = '2024-09-05T06:11:32.856Z'
    new_sotrudnik = api.post_employee(firname=FnameS, laname=lasName,
                                      MIDname=MidName, CompID=companyId, EMAIL=Mail)
    id = new_sotrudnik["id"]
    body = api.get_employee_ID(id)
    assert body["firstName"] == FnameS # проверяем имя созданного сотрудника
    # редактируем нового сотрудника
    lasName = 'Sergeev'                # меняем фамилию созданного сотрудника
    Mail = 'newstring@mail.com'        # меняем имэйл созданного сотрудника
    uRl = 'string'                     # меняем урл созданного сотрудника
    phone = 'string'                   # меняем телефон созданного сотрудника
    isActive = False                   # меняем активность созданного сотрудника
    client_redact = api.patch_employee_id(laname=lasName, EMAIL=Mail,
                                          URL=uRl, PHONE=phone, ISACT=isActive)
    # получаем инфо о сотруднике после редактирования по id
    id = client_redact["id"]
    body = api.get_employee_ID(id)
    assert body["lastName"] == lasName   # проверяем фамилию
    assert body["email"] == Mail         # проверяем имэйл
    assert body["isActive"] == isActive  # проверяем активность
    
@pytest.mark.test_negative  # все поля пустые (не проходит с пустыми полями)
@pytest.mark.xfail
def test_patch_employee_fail1():
    # создаем новую компанию
    name = 'NEW CITY'
    descript = 'CITY NEW'
    new_company = apiComp.create_company(name=name, description=descript)
    new_id = new_company["id"]
    # создаем и добавляем нового сотрудника
    FnameS = 'Nikolai'
    lasName = 'Nikolaev'
    MidName = 'Nikolaevich'
    companyId = new_id
    Mail = 'string@mail.com'
    uRl = 'string'
    phone = 'string'
    birthdate = '2024-09-05T06:11:32.856Z'
    new_sotrudnik = api.post_employee(firname=FnameS, laname=lasName,
                                      MIDname=MidName, CompID=companyId, EMAIL=Mail)
    id = new_sotrudnik["id"]
    body = api.get_employee_ID(id)
    assert body["firstName"] == FnameS  # проверяем имя созданного сотрудника
    # редактируем нового сотрудника
    lasName = ''                        # меняем фамилию созданного сотрудника
    Mail = ''                           # меняем имэйл созданного сотрудника
    uRl = ''                            # меняем урл созданного сотрудника
    phone = ''                          # меняем телефон созданного сотрудника
    isActive = False                    # меняем активность созданного сотрудника
    client_redact = api.patch_employee_id(id, laname=lasName, EMAIL=Mail,
                                          URL=uRl, PHONE=phone, ISACT=isActive)
    # получаем инфо о сотруднике после редактирования по id
    id = client_redact["id"]
    body = api.get_employee_ID(id)
    assert body["lastName"] == lasName    # проверяем фамилию
    assert body["email"] == Mail          # проверяем имэйл
    assert body["isActive"] == isActive   # проверяем активность