import sqlite3


class Connection:
    def __init__(self):
        self.connect = sqlite3.connect('db.sqlite')
        self.cur = self.connect.cursor()

    def close(self):
        self.connect.close()


class Database(Connection):
    def create_database(self):
        q = """
                CREATE TABLE IF NOT EXISTS phonebook (
                  id INTEGER PRIMARY KEY AUTOINCREMENT,
                  name VARCHAR(50),
                  surname VARCHAR(50),
                  patronymic VARCHAR(50),
                  organization VARCHAR(50),
                  work_phone VARCHAR(15),
                  personal_phone VARCHAR(15)
                );
            """

        self.cur.execute(q)

    def drop_table(self):
        q = """
                DROP TABLE phonebook;
            """
        self.cur.execute(q)

    def get_data(self) -> list:
        q = """
                SELECT * FROM phonebook;
            """
        results = self.cur.execute(q)
        return list(results)

    def push_data(self, value: tuple):
        q = """
                INSERT INTO phonebook
                (name, surname, patronymic,
                organization, work_phone, personal_phone)
                VALUES(?, ?, ?, ?, ?, ?);
            """
        self.cur.execute(q, value)
        self.connect.commit()

    def get_personal_data(self, personal_id) -> list:
        q = f"""
                SELECT * FROM phonebook
                WHERE id = {personal_id}
            """
        result = self.cur.execute(q)
        return list(result)

    def remake_personal_data(self, personal_id: int, value: tuple):
        q = f"""
                UPDATE phonebook
                SET surname = ?,
                    name = ?,
                    patronymic = ?,
                    organization = ?,
                    work_phone = ?,
                    personal_phone = ?
                WHERE id = {personal_id}
            """
        self.cur.execute(q, value)
        self.connect.commit()

    def filtered_data(self, kwargs):
        q = "SELECT * FROM phonebook WHERE "
        for key, value in kwargs.items():
            q += f'{key} LIKE "{value}"' if q.endswith(' ') else f' and {key} LIKE "{value}"'
        result = self.cur.execute(q)
        return list(result)

