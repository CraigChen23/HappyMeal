import sqlite3
from flask import Flask, render_template, redirect, session, request, url_for


app = Flask(__name__)
app.secret_key = "super"

'''METHODS============================================================='''

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

create_users_db()

'''FLASK================================================='''

'''
root route, renders the login page
'''
@app.route("/", methods=['GET', 'POST'])
def disp_loginpage():
    if 'username' in session: #home page rendered if there is a session
        return render_template('home.html', msg="successfully logged in")
    return render_template('login.html')

'''
login route, checks if attempted login matches data in the
database
- if yes --> user goes to home
- if no --> user gets login page with error messages
'''
@app.route("/login", methods =['GET', 'POST'])
def authenticate():
    user = request.form['username']
    passw = request.form['password']
    #print(db.valid_login(user, passw))

    if valid_login(user, passw):
        session['username'] = user
        return render_template('home.html', msg = "successfully logged in")
    else:
        return render_template('login.html', msg="login failed")

'''
register route, allows user to create a new account
'''
@app.route("/register", methods=['GET','POST'])
def register_account():
    if request.method == 'GET':
        return render_template('register.html')
    user = request.form['newUser']
    #user = request.form.get('newUser')
    passw = request.form['newPass']
    #passw = request.form.get('newPass')

    if user_exists(user):
        return render_template('register.html', msg="username is in use!")
    else:
        add_user(user, passw)
        return render_template('login.html', msg = "user registered!, log in with your new credentials.")

@app.route("/logout", methods=['GET', 'POST'])
def log_out():
    session.pop('username', None)
    return redirect('/')

@app.errorhandler(500)
def no_info():
    return render_template('noinfo.html'), 500
#================================================#

if __name__ == "__main__":  # true if this file NOT imported
    app.debug = True        # enable auto-reload upon code change
    app.run()