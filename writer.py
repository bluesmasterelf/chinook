"""Module contains all functions which write to the database, including admin functions and createUser
"""
import sqlite3
from login import hashFunction


class Writer(Reader): 
    """Create/Delete for the database itself, CRUD for users within the database, CRUD for the library data
    """
          

    def createTable(database):
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

    def createAdmin(database):
        connection = sqlite3.connect(database)
        cursor = connection.cursor()

        encrypted=hashFunction(input('Type admin password:'))

        format_str = """INSERT INTO users (user_id, username, encryptedPWD, privileges) VALUES (NULL, "admin", "{encrypt}", "admin")
        """
        sql_command=format_str.format(encrypt=encrypted)
        cursor.execute(sql_command)

        connection.commit()
        connection.close()

    def createUser(): 
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

        sql_command = format_str.format(first=user_info[0], password=user_info[1])
        cursor.execute(sql_command)

        connection.commit()
        connection.close()
    #def editUser(database, hashFunction): 
    #def deleteUser(database, hashFunction): 

    #def addBook():
    #def editBook():





if __name__=='__main__':

    database="chinook.db"
    writer=Writer(database)
    writer.createuser()

