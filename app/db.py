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
    #c.execute("CREATE TABLE IF NOT EXISTS exports(country TEXT, 1990 REAL, 1991 REAL, 1992 REAL, 1993 REAL, 1994 REAL, 1995 REAL, 1996 REAL, 1997 REAL, 1998 REAL, 1999 REAL, 2000 REAL, 2001 REAL, 2002 REAL, 2003 REAL, 2004 REAL, 2005 REAL, 2006 REAL, 2007 REAL, 2008 REAL, 2009 REAL, 2010 REAL, 2011 REAL, 2012 REAL, 2013 REAL, 2014 REAL, 2015 REAL, 2016 REAL, 2017 REAL, 2018 REAL)")
    c.execute("CREATE TABLE IF NOT EXISTS exports(country TEXT, 1990 REAL)")
    db.commit() #save changes
    db.close()  #close database

def populate_exports_db():

    DB_FILE="exports.db"
    db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
    c = db.cursor()
    #dict = {}
    #dict["country"] = []
    #dict["age"] = []
    #dict["id"] = []

    with open('exports.csv', 'r') as f:
        reader =  csv.DictReader(f)
        dict = []

        for row in reader:
            dict.append(row)
            #dict["country"].append(row['country'])
            #dict["age"].append(row['age'])
            #dict["id"].append(row['id'])
            #things = row["country"]
            #command = "insert into exports values(things);"
            #command = "insert into student values ([studentDict["name"],studentDict["age"],studentDict["id"]])"
            #c.execute(command)

    for i in dict:
        c.execute("INSERT INTO exports VALUES('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(i['country'], i['1990'], i['1991'], i['1992'], i['1993'], i['1994'], i['1995'], i['1996'], i['1997'], i['1998'], i['1999'], i['2000'], i['2001'], i['2002'], i['2003'], i['2004'], i['2005'], i['2006'], i['2007'], i['2008'], i['2009'], i['2010'], i['2011'], i['2012'], i['2013'], i['2014'], i['2015'], i['2016'], i['2017'], i['2018']))
    
    command = ""
    c.execute(command)

    db.commit()
    db.close()


create_exports_db()
populate_exports_db()