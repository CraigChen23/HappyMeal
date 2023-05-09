#database file

import sqlite3
import csv

'''USERS==================================================================='''

'''create user'''
def create_users_db():
    DB_FILE="users.db"

    db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create it
    c = db.cursor()               #facilitate db ops -- you will use cursor to trigger db events
    # users table
    c.execute("CREATE TABLE IF NOT EXISTS users(user TEXT, pass TEXT)")

    db.commit() #save changes
    db.close()  #close database

'''
Adds a user into the user.db file given username and password
*string user
*string password
'''
def add_user(user, passw):
    DB_FILE="users.db"

    db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
    c = db.cursor()               #facilitate db ops -- you will use cursor to trigger db events

    # add newly registered people in
    c.execute("INSERT INTO users (user, pass) VALUES (?,?)", (user, passw))

    #prints users table
    table = c.execute("SELECT * from users")
    print("user table from add_user() call")
    print(table.fetchall())

    db.commit() #save changes
    db.close()  #close database


'''
Used for user.db
Checks if login credentials match any in the database
'''
def valid_login(user, passw):
    DB_FILE="users.db"
    db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
    c = db.cursor()               #facilitate db ops -- you will use cursor to trigger db events

    # check if username is in table
    username = c.execute("SELECT user FROM users WHERE user = ?", (user,)).fetchone()

    if username is None:
        exists = False
    else:
        exists = True

    # check if password is in table
    password = c.execute("SELECT pass FROM users WHERE pass =?", (passw,)).fetchone()
    if password is None:
        exists = False

    db.commit() #save changes
    db.close()  #close database
    return exists

def user_exists(user):
    DB_FILE="users.db"
    db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
    c = db.cursor()               #facilitate db ops -- you will use cursor to trigger db events

    username = c.execute("SELECT user FROM users WHERE user = ?", (user,)).fetchone()

    if username is None:
        exists = False
    else:
        exists = True

    db.commit() #save changes
    db.close()  #close database
    return exists

'''COFFEE EXPORTS================================================='''

'''create exports db'''
def create_exports_db():
    DB_FILE="exports.db"

    db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create it
    c = db.cursor()               #facilitate db ops -- you will use cursor to trigger db events
    # users table
    c.execute("CREATE TABLE IF NOT EXISTS exports(country TEXT, 1990 INTEGER, 1991 INTEGER, 1992 INTEGER, 1993 INTEGER, 1994 INTEGER, 1995 INTEGER, 1996 INTEGER, 1997 INTEGER, 1998 INTEGER, 1999 INTEGER, 2000 INTEGER, 2001 INTEGER, 2002 INTEGER, 2003 INTEGER, 2004 INTEGER, 2005 INTEGER, 2006 INTEGER, 2007 INTEGER, 2008 INTEGER, 2009 INTEGER, 2010 INTEGER, 2011 INTEGER, 2012 INTEGER, 2013 INTEGER, 2014 INTEGER, 2015 INTEGER, 2016 INTEGER, 2017 INTEGER, 2018 INTEGER)")

    db.commit() #save changes
    db.close()  #close database
'''
def populate_exports_db():

    dict = {}
    dict["country"] = []
    #dict["age"] = []
    #dict["id"] = []

    with open('exports.csv') as f:
        r =  csv.DictReader(f)
        for row in r:
            dict["country"].append(row['country'])
            #dict["age"].append(row['age'])
            #dict["id"].append(row['id'])
            things = row["country"]
            command = "insert into exports values(things);"
            #command = "insert into student values ([studentDict["name"],studentDict["age"],studentDict["id"]])"
            #c.execute(command)
print(dict)

#insert = "INSERT INTO student (name, age, id) VALUES (?,?,?)",[studentDict["name"],studentDict["age"],studentDict["id"]]
select = "SELECT * FROM exports"

#c.execute(insert)
rows = c.execute(select).fetchall()
for r in rows:
    print (r)


command = ""          # test SQL stmt in sqlite3 shell, save as string
c.execute(command)    # run SQL statement
'''