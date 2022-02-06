import mysql.connector
from datetime import datetime


class DatabaseCommand:

    def __init__(self):
        self.db = mysql.connector.connect(
            host="remotemysql.com",
            user="5jBdUHTRPG",
            passwd = "QPMKcvQU51",
            database="5jBdUHTRPG"
        )

        self.mycursor = self.db.cursor()

    
    def create_database(self, name):
        self.mycursor.execute(f"CREATE DATABASE {name}")
        self.mycursor.execute(f"USE {name}")

    def create_table(self, tablename, values):
        self.mycursor.execute(f"CREATE TABLE IF NOT EXISTS {tablename} {values}")

    def describe(self, tablename):
        self.mycursor.execute(f"DESCRIBE {tablename}")
        for x in self.mycursor:
            print(x)

    def insert(self, tablename, values, columns=None):
        if not columns:
            print(f"INSERT INTO {tablename} VALUES {values}")
            self.mycursor.execute(f"INSERT INTO {tablename} VALUES {values}")
        else:
            self.mycursor.execute(f"INSERT INTO {tablename} {columns} VALUES {values}")
        self.db.commit()
        # self.display_table(tablename)

    def create_dict(self, tablename):
        self.mycursor.execute(f"SELECT * FROM {tablename}")
        records = self.mycursor.fetchall()
        d = {}
        for row in records:
            d[row[0]] = row[1]
        return d

    def filter(self, tablename, column_names, where=None, group_by=None, having=None, order_by=None):
        self.mycursor.execute(f"SELECT {column_names} FROM {tablename}")

    def other(self):
        self.mycursor.execute("")
        for x in self.mycursor:
            print(x)

obj = DatabaseCommand()
obj.other()
