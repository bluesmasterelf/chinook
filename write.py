"""Module contains all functions which write to the database, including admin functions and createUser
"""
import sqlite3
from login import hashFunction


def createUser(database):
    """Accepts a database, prompts user for new username and password, writes them to database and returns to login.
    """
    connection = sqlite3.connect(database)
    cursor = connection.cursor()

    passwordMatch=False
    while not passwordMatch:

        username=input('enter username:')
        password=input('enter password:')
        password2=input('Enter password again, I do not trust you:')
        if password==password2:
            passwordMatch=True
        else:
            print('Epic fail. Learn to type, bro')


    password=hashFunction(password)
    user_info = [ (username, password, notAdmin) ]
    format_str = """INSERT INTO users (user_id, username, password, privileges)
    VALUES (NULL, "{username}", "{password}", "user");"""

    sql_command = format_str.format(first=user_info[0], password=user_info[1], gender=p[\
2])
    cursor.execute(sql_command)

    connection.commit()
    connection.close()

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
