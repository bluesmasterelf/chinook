"""Module contains all functions which write to the database, including admin functions and createUser
"""
import sqlite3
from login import hashFunction


class writer(): #writer should inherit from reader so that reader functions are present without duplicating code

    def insert(database, adminToken=False):
        """Handles all database write functions, requires adminToken to be passed for security.
        """
        if not adminToken:
            return 1

        option2=input("Would you like to insert data into this set?")
        if option2=="yes":
            print("sorry, that resource hasn't been coded yet.")
            #most of the syntax is above, need to build options--check diagram

    def create(database):
        """Creates table 'users' Otherwise, tables should be created by the DBA.
        """
        connection = sqlite3.connect(database)
        cursor = connection.cursor()

        sql_command="""
    CREATE TABLE users (
    user_id INTEGER PRIMARY KEY,
    username VARCHAR(20),
    encryptedPWD INTEGER,
    privileges VARCHAR(5));"""
        cursor.execute(sql_command)
        connection.commit()
        connection.close()

    def admin(database):
        connection = sqlite3.connect(database)
        cursor = connection.cursor()

        encrypted=hashFunction(input('Type admin password:'))

        format_str = """INSERT INTO users (user_id, username, encryptedPWD, privileges) VALUES (NULL, "admin", "{encrypt}", "admin")
        """
        sql_command=format_str.format(encrypt=encrypted)
        cursor.execute(sql_command)

        connection.commit()
        connection.close()

if __name__=='__main__':
#test code
    #create("chinook.db")
    admin("chinook.db")
