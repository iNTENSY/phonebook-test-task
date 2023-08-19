import csv
import json


class Database:
    @staticmethod
    def create_database():
        with open('db.json', 'w', encoding='utf-8') as jsonfile:
            pass

    @staticmethod
    def get_data() -> list:
        database = open('db.json', 'r', encoding='utf-8')
        reader = json.load(database)
        database.close()
        return reader


    def push_data(self, value: list):
        last_id: int = int(max(self.get_data(), key = lambda row: int(row[0]))[0])
        value.insert(0, last_id + 1)
        print(f'Добавляю: {value}')
        with open('db.csv', 'a+', encoding='utf-8', newline='') as jsonfile:
            json.dump(value, jsonfile)



    @staticmethod
    def push_test_data():
        with open('db.json', 'w', encoding='utf-8') as jsonfile:
            userdata = [
                {
                    'id': 0,
                    'surname': '-',
                    'first_name': '-',
                    'patronymic': '-',
                    'organization': '-',
                    'work_phone': 777,
                    'personal_phone': 888,
                },
                {
                    'id': 1,
                    'surname': 'Имя1',
                    'first_name': 'Фамилия1',
                    'patronymic': 'Отчество1',
                    'organization': 'Организация1',
                    'work_phone': 111,
                    'personal_phone': 110,
                },
                {
                    'id': 2,
                    'surname': 'Имя2',
                    'first_name': 'Фамилия2',
                    'patronymic': 'Отчество2',
                    'organization': 'Организация2',
                    'work_phone': 222,
                    'personal_phone': 221,
                },
                {
                    'id': 3,
                    'surname': 'Имя3',
                    'first_name': 'Фамилия3',
                    'patronymic': 'Отчество3',
                    'organization': 'Организация3',
                    'work_phone': 333,
                    'personal_phone': 332,
                },
            ]
            json.dump(userdata, jsonfile, indent=4)