import os

from prettytable import PrettyTable

import db as database



class Phonebook:
    PAGINATE_BY: int = 5
    FIELD_NAMES: tuple[str] = ('ID', 'Фамилия', 'Имя', 'отчество', 'Организация', 'Рабочий телефон', 'Личный телефон')

    def __new__(cls, *args, **kwargs):
        print('\nВы запустили телефонный справочник!')
        return super().__new__(cls, *args, **kwargs)

    def __init__(self):
        self.clear_console()
        self.information()


    def information(self) -> None:
        message: str = ('Перед вами список основных возможностей:\n'
                        '1. Вывод постранично записей из справочника на экран\n'
                        '2. Добавление новой записи в справочник\n'
                        '3. Возможность редактирования записей в справочнике\n'
                        '4. Поиск записей по одной или нескольким характеристикам\n')
        print(message)
        self.command_handler()


    def command_handler(self) -> None:
        command = input('Введите требуемую команду: ')
        command_types = {
            '1': self.list_of_records,
            '2': self.add_data
        }
        command_types[command]()


    def list_of_records(self, page: int = 1, data: list = None):
        self.clear_console()
        print('Чтобы вернуться обратно введите: *')

        if data is None:
            data = database.Database.get_data()

        table = self.make_table(page, data)
        print(table)

        command = input('>> ')
        if command == '*':
            self.information()
        elif command.isdigit():
            self.list_of_records(int(command), data=data)


    def add_data(self):
        self.clear_console()

        data = database.Database()

        surname: str = input('Введите фамилию >> ')
        first_name: str = input('Введите имя >> ')
        patronymic: str = input('Введите отчество >> ')
        organization: str = input('Введите организацию >> ')
        work_phone: str = input('Введите рабочий телефон >> ')
        personal_phone: str = input('Введите личный телефон >> ')

        data.push_data(value=[surname, first_name, patronymic, organization, work_phone, personal_phone])

        self.list_of_records()




    def make_table(self, page: int, data: list):
        index: int = self.PAGINATE_BY * page
        table = PrettyTable()
        table.field_names = self.FIELD_NAMES
        for row in range(index - self.PAGINATE_BY, index if index <= len(data) else len(data)):
            table.add_row(data[row])
        return table


    @staticmethod
    def clear_console():
        os.system('cls')



if __name__ == '__main__':
    db = database.Database()
    if not os.path.exists('db.csv'):
        db.create_database()
        db.push_test_data()
    Phonebook()
