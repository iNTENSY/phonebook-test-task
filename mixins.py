import os
from time import sleep

from prettytable import PrettyTable


def input_util():
    surname: str = input('Введите фамилию >> ')
    first_name: str = input('Введите имя >> ')
    patronymic: str = input('Введите отчество >> ')
    organization: str = input('Введите организацию >> ')
    work_phone: str = input('Введите рабочий телефон >> ')
    personal_phone: str = input('Введите личный телефон >> ')
    return [surname, first_name, patronymic,
            organization, work_phone, personal_phone]


class CommandHandlerMixin:
    """
    Данный класс используется в качестве обработчика команд.
    """
    def command_handler(self) -> None:
        command: str = input('Введите требуемую команду: ')
        types = {
            '': exit,
            '1': self.get_list_data,
            '2': self.add_data,
            '3': self.edit_personal_page
        }
        types[command]() if command in types.keys() else types['']()

    def get_list_data(self):
        raise NotImplementedError('Переопределите метод "get_list_data"')

    def add_data(self):
        raise NotImplementedError('Переопределите метод "add_data"')

    def edit_personal_page(self):
        raise NotImplementedError('Переопределите метод "edit_personal_page"')


class MessageHandlerMixin:
    """
    Данный класс позволяет реализовать методы отрисовки данных в консоль.
    """
    PAGINATE_BY: int = 2
    FIELD_NAMES: tuple[str] = (
        'ID', 'Имя', 'Фамилия', 'отчество',
        'Организация', 'Рабочий телефон', 'Личный телефон'
    )

    def print_table(self, page: int = 1, data: list = None) -> None:
        """
        Данный метод печатает таблицу в соответствии со страницей.
        """
        self.clear_console()
        print(self.make_table(page=page, data=list(data)))
        print('Нажмите "Enter" чтобы вернуться')

    def make_table(self,
                   page: int = 1,
                   data: list = None,
                   is_personal: bool = False) -> PrettyTable:
        """
        Данный метод создает и возвращает таблицу с учетом пагинации.
        """
        table = PrettyTable()
        table.field_names = self.FIELD_NAMES

        index: int = self.PAGINATE_BY * page
        start: int = index - self.PAGINATE_BY
        stop: int = index if index <= len(data) else len(data)

        if not is_personal:
            for row in range(start, stop):
                table.add_row(data[row])
        else:
            table.add_row(data[0])
        return table

    def send_information(self) -> None:
        """
        Данный метод печатает в консоль информацию
        о возможных стандартных действий с телефонным справочником.
        """
        self.clear_console()
        message: str = (
            'Перед вами список основных возможностей:\n'
            '1. Вывод постранично записей из справочника на экран\n'
            '2. Добавление новой записи в справочник\n'
            '3. Возможность редактирования записей в справочнике\n'
            '4. Поиск записей по одной или нескольким характеристикам\n'
        )
        print(message)
        self.command_handler()

    def get_list_data(self, page: int = 1, data: list = None) -> None:
        """
        Данный метод позволяет пользователю исследовать
        свой телефонный справочник на наличие записей.
        """
        self.clear_console()

        queryset = self.db.get_data()
        self.print_table(page=page, data=queryset)

        command = input('Номер страницы >> ')
        (self.get_list_data(int(command), data=data)
         if command.isdigit() else self.send_information())

    @staticmethod
    def clear_console():
        os.system('cls')
        print('\n')


class DataEditorMixin:
    """
    Данный класс позволяет манипулировать данными.
    """
    def edit_personal_page(self):
        """Данный метод позволяет изменять запись в справочнике."""
        self.clear_console()
        personal_id: int = int(input('Введите ID записи >> '))

        personal_info = self.db.get_personal_data(personal_id)
        if personal_info:
            print(self.make_table(is_personal=True, data=personal_info))
            edited_values = input_util()
            self.db.remake_personal_data(
                personal_id=personal_id, value=edited_values
            )
        else:
            print('Данного ID не существует! '
                  'Через 5 секунд вы будете перенаправлены!')
            sleep(5)
        self.send_information()

    def add_data(self):
        """Данный метод позволяет добавлять запись в телефонный справочник."""
        self.clear_console()
        values = input_util()
        self.db.push_data(value=values)
        self.send_information()

    def clear_console(self) -> None:
        raise NotImplementedError('Переопределите метод "clear_console"')

    def send_information(self) -> None:
        raise NotImplementedError('Переопределите метод "send_information"')

    def make_table(self, is_personal, data) -> PrettyTable:
        raise NotImplementedError('Переопределите метод "make_table"')
