import mysql.connector
from datetime import datetime

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="PrIv@MySQL",
    database="testbase"
)

mycursor = db.cursor()

'''
def CreateDatabase(name):
    mycursor.execute(f"CREATE DATABASE {name}")
'''

def CreateTable(tablename, values):
    mycursor.execute(f"CREATE TABLE {tablename} {values}")

def Describe(tablename):
    mycursor.execute(f"DESCRIBE {tablename}")
    for x in mycursor:
        print(x)

def Insert(tablename, values, columns=None):
    if columns == None:
        mycursor.execute(f"INSERT INTO {tablename} VALUES {values}")
    else:
        mycursor.execute(f"INSERT INTO {tablename} {columns} VALUES {values}")
    db.commit()
    DisplayTable(tablename)

def DisplayTable(tablename, i="*"):
    mycursor.execute(f"SELECT {i} FROM {tablename}")
    for x in mycursor:
        print(x)

def filter(tablename, column_names, where=None, group_by=None, having=None, order_by=None):
    mycursor.execute(f"SELECT {column_names} FROM {tablename}")

def Other(query):
    mycursor.execute(query)

