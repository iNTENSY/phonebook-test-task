import csv


class Database:
    @staticmethod
    def create_database():
        with open('db.csv', 'w', encoding='utf-8', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(
                ('Фамилия', 'Имя', 'Отчество', 'Организация', 'Рабочий телефон', 'Личный телефон')
            )

    @staticmethod
    def get_data() -> list:
        with open('db.csv', 'r', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            return list(reader)[1:]


    def push_data(self, value: list):
        last_id: int = int(max(self.get_data(), key = lambda row: int(row[0]))[0])
        value.insert(0, last_id + 1)
        print(f'Добавляю: {value}')
        with open('db.csv', 'a+', encoding='utf-8', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=',')
            writer.writerow(value)



    @staticmethod
    def push_test_data():
        with open('db.csv', 'a+', encoding='utf-8', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=',')
            userdata = [
                ['0', '-', '-', '-', '-', '777', '888'],
                ['1', 'Имя1', 'Фамилия1', 'Отчество1', 'Организация1', 'Раб. номер1', 'Личн. номер1'],
                ['2', 'Имя2', 'Фамилия2', 'Отчество2', 'Организация2', 'Раб. номер2', 'Личн. номер2'],
                ['3', 'Имя3', 'Фамилия3', 'Отчество3', 'Организация3', 'Раб. номер3', 'Личн. номер3'],
                ['4', 'Имя4', 'Фамилия4', 'Отчество4', 'Организация4', 'Раб. номер4', 'Личн. номер4'],
                ['5', 'Имя5', 'Фамилия5', 'Отчество5', 'Организация5', 'Раб. номер5', 'Личн. номер5'],
                ['6', 'Имя6', 'Фамилия6', 'Отчество6', 'Организация6', 'Раб. номер6', 'Личн. номер6'],
                ['7', 'Имя7', 'Фамилия7', 'Отчество7', 'Организация7', 'Раб. номер7', 'Личн. номер7'],
                ['8', 'Имя8', 'Фамилия8', 'Отчество8', 'Организация8', 'Раб. номер8', 'Личн. номер8'],
                ['9', 'Имя9', 'Фамилия9', 'Отчество9', 'Организация9', 'Раб. номер9', 'Личн. номер9'],
            ]
            writer.writerows(userdata)