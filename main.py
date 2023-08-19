import os

import db as database
from mixins import MessageHandlerMixin, CommandHandlerMixin, DataEditorMixin


class Phonebook(
    MessageHandlerMixin,
    DataEditorMixin,
    CommandHandlerMixin
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
