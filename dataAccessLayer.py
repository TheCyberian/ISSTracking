__author__ = 'utkarsh_raghav'
import sqlite3


class DataAccessLayer:
    def __init__(self):
         with sqlite3.connect("APIData.db", check_same_thread=False) as connection:
          self.c = connection.cursor()


    def fetch_last_known_locations_data(self):
        self.c.execute("SELECT * FROM ApiDataTableDemo")
        rows = self.c.fetchall()
        return rows


    def fetch_last_known_n_location_data(self, num):
        self.c.execute("SELECT * FROM ApiDataTableDemo")
        rows = self.c.fetchmany(num)
        return rows


    def fetch_pass_by_time(self):
        self.c.execute("SELECT * FROM PassbyDataTableDemo")
        rows = self.c.fetchall()
        return rows


    def fetch_pass_by_n_times(self, num):
        self.c.execute("SELECT * FROM PassbyDataTableDemo")
        rows = self.c.fetchmany(num)
        return rows
