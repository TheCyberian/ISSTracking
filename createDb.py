__author__ = 'utkarsh_raghav'

import sqlite3


connection = sqlite3.connect("APIData.db")

c = connection.cursor()

c.execute("CREATE TABLE IF NOT EXISTS ApiDataTableDemo(time TEXT, lat REAL, long REAL)")
c.execute("CREATE TABLE IF NOT EXISTS PassbyDataTableDemo(time TEXT, duration TEXT)")

def insert_data():
    c.execute("INSERT INTO PassbyDataTableDemo VALUES('141223', '3614')")
    c.execute("INSERT INTO PassbyDataTableDemo VALUES('151224', '3823')")
    c.execute("INSERT INTO PassbyDataTableDemo VALUES('161225', '3532')")
    connection.commit()


insert_data()

def display_data():
    c.execute("SELECT * FROM PassbyDataTableDemo")
    rows = c.fetchall()
    print(rows)

display_data()
