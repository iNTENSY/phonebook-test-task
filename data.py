"""
Вы можете автоматически подгрузить данные в базу данных.
Данный действие можно повторять неограниченное количество раз.
"""
from db import Database

userdata = (
    ('Имя0', 'Фамилия0', 'Отчество0', 'Организация0', '0', '00'),
    ('Имя1', 'Фамилия1', 'Отчество1', 'Организация1', '1', '11'),
    ('Имя2', 'Фамилия2', 'Отчество2', 'Организация2', '2', '22'),
    ('Имя3', 'Фамилия3', 'Отчество3', 'Организация3', '3', '33'),
    ('Имя4', 'Фамилия4', 'Отчество4', 'Организация4', '4', '44'),
    ('Имя5', 'Фамилия5', 'Отчество5', 'Организация5', '5', '55'),
    ('Имя6', 'Фамилия6', 'Отчество6', 'Организация6', '6', '66'),
    ('Имя7', 'Фамилия7', 'Отчество7', 'Организация7', '7', '77'),
    ('Имя8', 'Фамилия8', 'Отчество8', 'Организация8', '8', '88'),
    ('Имя9', 'Фамилия9', 'Отчество9', 'Организация9', '9', '99'),
    ('Имя10', 'Фамилия10', 'Отчество10', 'Организация10', '10', '1010'),
)

if __name__ == '__main__':
    db = Database()
    db.create_database()
    cursor = db.cur
    query = """INSERT INTO phonebook
               (name, surname, patronymic, organization, work_phone, personal_phone)
               VALUES (?, ?, ?, ?, ?, ?);"""
    cursor.executemany(query, userdata)
    db.connect.commit()
    db.close()