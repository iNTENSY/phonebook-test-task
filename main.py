import abc
import json
import os

from prettytable import PrettyTable

import db as database



class InformationInt(abc.ABC):
    PAGINATE_BY: int = 2
    FIELD_NAMES: tuple[str] = (
        'ID', 'Фамилия', 'Имя', 'отчество',
        'Организация', 'Рабочий телефон', 'Личный телефон'
    )

    @abc.abstractmethod
    def make_table(self, page: int, data: list) -> PrettyTable:
        index: int = self.PAGINATE_BY * page
        table = PrettyTable()
        table.field_names = self.FIELD_NAMES
        for row in range(index - self.PAGINATE_BY, index if index <= len(data) else len(data)):
            table.add_row(data[row].values())
        return table


    @abc.abstractmethod
    def send_information(self) -> None:
        message: str = ('Перед вами список основных возможностей:\n'
                        '1. Вывод постранично записей из справочника на экран\n'
                        '2. Добавление новой записи в справочник\n'
                        '3. Возможность редактирования записей в справочнике\n'
                        '4. Поиск записей по одной или нескольким характеристикам\n')
        print(message)


class Phonebook(InformationInt):
    def __init__(self):
        print('\nВы запустили телефонный справочник!')
        self.clear_console()
        self.send_information()


    def command_handler(self) -> None:
        command = input('Введите требуемую команду: ')
        command_types = {
            '1': self.get_list_data,
            '2': self.add_data
        }
        command_types[command]()


    def get_list_data(self, page: int = 1, data: list = None):
        self.clear_console()

        if data is None:
            data = database.Database.get_data()

        self.make_table(page, data)

        command = input('>> ')
        if command == '*':
            self.send_information()
        elif command.isdigit():
            self.get_list_data(int(command), data=data)


    def add_data(self):
        self.clear_console()

        data = database.Database()

        surname: str = input('Введите фамилию >> ')
        first_name: str = input('Введите имя >> ')
        patronymic: str = input('Введите отчество >> ')
        organization: str = input('Введите организацию >> ')
        work_phone: str = input('Введите рабочий телефон >> ')
        personal_phone: str = input('Введите личный телефон >> ')

        data.push_data(
            value=[surname, first_name, patronymic, organization, work_phone, personal_phone]
        )

        self.get_list_data()


    def make_table(self, page: int, data: list) -> None:
        self.clear_console()
        table = super().make_table(page, data)
        print(table)
        print('Чтобы вернуться обратно введите: *')


    def send_information(self) -> None:
        self.clear_console()
        super().send_information()
        self.command_handler()


    @staticmethod
    def clear_console():
        os.system('cls')


if __name__ == '__main__':
    db = database.Database()
    if not os.path.exists('db.json'):
        db.create_database()
        db.push_test_data()
    # Phonebook()
    data = {
        "id": 4,
        "surname": "-",
        "first_name": "-",
        "patronymic": "-",
        "organization": "-",
        "work_phone": 777,
        "personal_phone": 888
    }
    with open('db.json', 'a', encoding='utf-8') as f:
        n = json.load(f)
        n.append(data)