import psycopg2
from pprint import pprint
from app import app


class DBConnection:
    def __init__(self):
        self.con = psycopg2.connect(database="stackover", user="postgres", password="keko", host="localhost",port="5432")
        self.con.autocommit = True
        self.cursor = self.con.cursor()
        self.dict_cursor = self.con.cursor(cursor_factory=extra.RealDictCursor)