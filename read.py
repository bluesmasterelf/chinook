"""Module for database reading functions
"""

import sqlite3

def read(database, loginToken=False):
    """Contains the database reading capabilities
    """
    if not loginToken:
        return -1

    connection = sqlite3.connect(database)
    cursor = connection.cursor()
    
    print("The options appear below.")
    cursor.execute("PRAGMA table_info(employees)")
    result = cursor.fetchall()    #Note: returns a list of tuples. Index 1=the data the user
        #is interested in. 0 is primary key, 2 is datatype et cetera            
    for r in result:
        print(r[1])
    option=input("What data would you like to view?")

    cursor.execute("SELECT "+ option+ " FROM employees")
    print("fetchall:")
    result = cursor.fetchall()
    for r in result:
        print(r[0])

    option2=input("press return")

    if option2=="test":
        print("Here's a join of the name and title columns of the artists and albums tables.")
        cursor.execute("SELECT Name, Title FROM artists INNER JOIN albums ON albums.Artistid\
=artists.ArtistId")
        res=cursor.fetchall()
        for r in res:
            print(r[0] + ':' + r[1])


if __name__=='__main__':

    loginToken=True
    database="chinook.db"
    read(database, loginToken)

