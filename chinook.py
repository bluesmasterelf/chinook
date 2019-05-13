import sqlite3
from login import login
from writer import writer
from read import read

class Interface:
    """Each instance should create a user interface that manages the sqlite3 commands for the user
    """
    def __init__(self, database):
        self.database=database
        self.user_type
        self.writer
        self.display
        

    def user_type(self):
        self.user_type=login()
        #login returns a user_type
       
    def display(self):
        bool loggedIn=false
        userExists=input('new or returning user? Select n/r')
        
        if userExists=='n':
            createUser()
        else:
            self.user_type=login()
            loggedIn=True
        
        
        while loggedIn:
            if self.user_type==admin:
                self.writer = writer()
                operation=input('Options include search, update, edit, delete, quit: s, u, e, d, q?')
                if operation=='s': read()
                
                elif operation=='q': loggedIn=false

                elif operation == 'e' or 'u' or 'd':
                    #writer.function calls? something or other

                else #throw exception

            elif self.user_type==user:
                operation=input('Options are search, quit: s, q?')
                
                if operation='q': loggedIn=false
                else read()
            else #throw exception

if __name__=='__main__':

    session=Interface("chinook.db")
    #session.access()
