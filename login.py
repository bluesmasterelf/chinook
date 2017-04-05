"""This module should contain the login utility and any necessary associated functions as they become needed. 
"""

import sqlite3
        
def hashFunction(string=None):
    """To serve as a password encryption function; irretrievable type. 
    """
    primes=[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59]    
    hashValue=1

    #choose a permutation to apply to string                                             
    

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

if __name__=='__main__':
    #test code

    print(hashFunction('word'))
    print(hashFunction('wore'))
    print('see, too close together, not chaotic enough')


