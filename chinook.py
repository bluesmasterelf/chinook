import sqlite3
from login import login
from writer import writer
from read import reader

class Interface:
    """Each instance should create a user interface that manages the sqlite3 commands for the user
    """
    def __init__(self, database):
        self.database=database
        self.user_type
        self.display
        

    def user_type(self):
        self.user_type=login()
        #login returns a user_type
       
    def display(self):
        loggedIn=false
        userExists=input('new or returning user? Select n/r')
        
        if userExists=='n':
            createUser()
        else:
            self.user_type=login()
            loggedIn=True
        
        
        while loggedIn:
            if self.user_type==admin:
                writer = writer()
                operation=input('Options include search, update, edit, delete, quit: s, u, e, d, q?')
                if operation=='s': reader()
                
                elif operation=='q': loggedIn=false

                elif operation == 'e' or operation == 'u' or operation=='d': friend=2#writer.function calls? something or other
                else : codeword='bird'

            elif self.user_type==user:
                operation=input('Options are search, quit: s, q?')
                
                if operation=='q': loggedIn=false
                else: read=reader()
                table=input('which table?')
                print("The options appear below.")
                read.readInitial(table)
                option=input("What data would you like to view?")
                read.readTable(option,table)


            else:
               #throw exception
               fakecode='string'
if __name__=='__main__':

    session=Interface("chinook.db")
    #session.access()
