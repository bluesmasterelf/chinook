"""This module should contain the login utility and any necessary associated functions as they become needed. 
"""

import sqlite3
      
def hashFunction(string=None):
    """To serve as a password encryption function; irretrievable type. 
    """
    primes=[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59]    
    hashValue=1

    #choose a permutation to apply to string           
    #
    #Add salt                                  
    
    for i in range(len(string)):
        iter=primes[i%17]**(ord(string[i])%13)
        hashValue=hashValue*iter
    return hashValue%(2**31)

def login(database, hashFunction):
    connection = sqlite3.connect(database)
    cursor = connection.cursor()
    loggedin=False
    while not loggedin:
        username=input('enter username:')
        password=input('enter password:')
            #sql query on logical key username, compare hash against stored value            
            #if sql.query(username)==self.hashFunction(password):                            
            #    return privileges         
            #  
    return user_type  
                                                          
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

if __name__=='__main__':
    #test code

    print(hashFunction('word'))
    print(hashFunction('wore'))
    print('see, too close together, not chaotic enough')


