import sqlite3
from login import hashFunction, login
from write import createUser, write
from read import read

class Interface:
    """Each instance should create a user interface that manages the sqlite3 commands for the user
    """
    def __init__(self, database, login, read, write):
        self.database=database
        self.loginToken=False
        

    def access(self):
        if self.loginToken==admin:
            #retrieve the names of the tables available, present to admin...
            return things
        else:
            print('gtfo newb')
            #smaller subset of admissible actions


if __name__=='__main__':

    session=Interface("chinook.db")
    userExists=input('new or returning user? Select n/r')
    if userExists=='n':
        session.createUser()
    else:
        access=session.login()
    #session.access()
