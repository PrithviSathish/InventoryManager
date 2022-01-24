import mysql.connector
from datetime import datetime


class DatabaseCommand:

    def __init__(self, user=None):
        self.db = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="PrIv@MySQL",
            database=user
        )

        self.mycursor = self.db.cursor()

    def create_database(self, name):
        self.mycursor.execute(f"CREATE DATABASE {name}")
        self.mycursor.execute(f"USE {name}")

    def create_table(self, tablename, values):
        self.mycursor.execute(f"CREATE TABLE {tablename} {values}")

    def describe(self, tablename):
        self.mycursor.execute(f"DESCRIBE {tablename}")
        for x in self.mycursor:
            print(x)

    def insert(self, tablename, values, columns=None):
        if not columns:
            self.mycursor.execute(f"INSERT INTO {tablename} VALUES {values}")
        else:
            self.mycursor.execute(f"INSERT INTO {tablename} {columns} VALUES {values}")
        self.db.commit()
        self.display_table(tablename)

    def display_table(self, tablename, i="*"):
        self.mycursor.execute(f"SELECT {i} FROM {tablename}")
        for x in self.mycursor:
            print(x)

    def filter(self, tablename, column_names, where=None, group_by=None, having=None, order_by=None):
        self.mycursor.execute(f"SELECT {column_names} FROM {tablename}")

    def other(self, query):
        self.mycursor.execute(query)
