import psycopg2
import os
from app.config import app_config

from pprint import pprint


class DatabaseConnection():

    def __enter__(self):
        try:
            if app_config['testing']:
                self.conn = psycopg2.connect("dbname = 'test_db' user = 'postgres' host = 'localhost' password = 'kekotowns' port = '5432'")         
                self.cursor = self.conn.cursor()
                return self.cursor
            else:
                self.conn = psycopg2.connect("dbname = 'stackoverlite' user = 'postgres' host = 'localhost' password = 'k3ko' port = '5432'")
                self.cursor = self.conn.cursor()
                return self.cursor
        except (Exception, psycopg2.DatabaseError) as error:
            pprint(error)
    
    def __exit__(self, exception_type, exception_val, exception_traceback):
        self.conn.commit()
        self.cursor.close()
        self.conn.close()
    
    