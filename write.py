"""Module contains all functions which write to the database, including admin functions and createUser
"""
import sqlite3
from login import hashFunction


def createUser(database, hashFunction):
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
            print('Epic fail, learn to type bro')


    password=hashFunction(password)
    user_info = [ (username, password, notAdmin) ]
    format_str = """INSERT INTO users (user_id, username, password, privileges)          
    VALUES (NULL, "{username}", "{password}", "{privileges}", "{birthdate}");"""

    sql_command = format_str.format(first=user_info[0], password=user_info[1], gender=p[\
2], birthdate = p[3])
    cursor.execute(sql_command)

    connection.commit()
    connection.close()

def write(database, adminToken=False):
    """Handles all database write functions, requires adminToken to be passed for security.
    """
    if not adminToken:
        return 1
    
    option2=input("Would you like to insert data into this set?")
    if option2=="yes":
        print("sorry, that resource hasn't been coded yet.")
        #most of the syntax is above, need to build options--check diagram



if __name__=='__main__':
#test code
