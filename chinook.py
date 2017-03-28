import sqlite3

class Interface:
    """Each instance should create a user interface that manages the sqlite3 commands for the user
    """
    def __init__(self, database):
        self.database=database
        self.loginToken=None
        self.primes=[2,3,5,7,11,13,17,19,23,29,31,37,41]

    def hashFunction(string=None):
        hashValue=1
        #choose a permutation to apply to string
        for i in range(len(string)):
            iter=self.primes[i]**ord(string[i])  
            hashValue=hashValue*iter
        return hashValue%(10**10)

    def createUser(self):
        connection = sqlite3.connect(self.database)
        cursor = connection.cursor()
        username=input('enter username:')
        password=input('enter password (13 characters recommended)')
        password=self.hashFunction(password)
        user_info = [ (username, password, notAdmin) ]       
        format_str = """INSERT INTO users (user_id, username, password, privileges)
    VALUES (NULL, "{username}", "{password}", "{privileges}", "{birthdate}");"""

        sql_command = format_str.format(first=user_info[0], password=user_info[1], gender=p[2], birthdate = p[3])
        cursor.execute(sql_command)

        connection.commit()
        connection.close()


    def login(self):
        connection = sqlite3.connect(self.database)
        cursor = connection.cursor()
        loggedin=False
        while not loggedin:
            username=input('enter username:')
            password=input('enter password:')
            #sql query on logical key username, compare hash against stored value
            #if sql.query(username)==self.hashFunction(password):
            #    return privileges

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
    

    connection = sqlite3.connect("chinook.db")
    cursor = connection.cursor()
    
    print("The options appear below.")
    cursor.execute("PRAGMA table_info(employees)")
    result = cursor.fetchall()    #Note: returns a list of tuples. Index 1=the data the user is interested in. 0 is primary key, 2 is datatype et cetera
    for r in result:
        print(r[1])
    option=input("What data would you like to view?")

    cursor.execute("SELECT "+ option+ " FROM employees")
    print("fetchall:")
    result = cursor.fetchall()
    for r in result:
        print(r[0])

    option2=input("Would you like to insert data into this set?")
    if option2=="yes":
        print("sorry, that resource hasn't been coded yet.")

    input("press return")
    print("Here's a join of the name and title columns of the artists and albums tables.")
    
    if option2=="no":
        cursor.execute("SELECT Name, Title FROM artists INNER JOIN albums ON albums.Artistid=artists.ArtistId")
        res=cursor.fetchall()
        for r in res:
            print(r[0] + ':' + r[1])
