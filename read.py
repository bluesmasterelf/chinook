"""Module for database reading functions
"""

import sqlite3
  
class Reader:
    """Contains the database reading capabilities
    """
    def __init__(self, database):
        self.database=database
        self.connection = sqlite3.connect(self.database)
        self.cursor = self.connection.cursor()
   
    def readTable(self, table):
        self.cursor.execute("PRAGMA table_info("+table+")")
        result = self.cursor.fetchall()    #Note: returns a list of tuples. Index 1=the data the user
            #is interested in. 0 is primary key, 2 is datatype et cetera
        for r in result:
            print(r[1])

    
    def readColumn(self, option, table):
        self.cursor.execute("SELECT "+ option+ " FROM " + table)
        print("fetchall:")
        result = self.cursor.fetchall()
        for r in result:
            print(r[0])

    

    def test(self):
        print("Here's a join of the name and title columns of the artists and albums tables.")
        self.cursor.execute("SELECT Name, Title FROM artists INNER JOIN albums ON albums.Artistid=artists.ArtistId")
        res=self.cursor.fetchall()
        for r in res:
            print(r[0] + ':' + r[1])


if __name__=='__main__':

    database="chinook.db"
    reader=Reader(database)
    operation=input('Options are search, quit: s, q?')
                
    if operation=='q': loggedIn=false
    else: 
        table=input('which table?')
        print("The options appear below.")
        reader.readTable(table)
        option=input("What data would you like to view?")
        reader.readColumn(option,table)

        option2=input('press return')
        if option2=='test': reader.test()
