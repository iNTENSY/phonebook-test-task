import os

import db as database
from mixins import MessageHandler, CommandHandler, DataHandler


class Phonebook(
    MessageHandler,
    DataHandler,
    CommandHandler
):
    def __init__(self):
        self.db = database.Database()
        self.clear_console()
        self.send_information()


if __name__ == '__main__':
    if not os.path.exists('db.sqlite'):
        db = database.Database()
        db.create_database()
        db.close()
    Phonebook()
