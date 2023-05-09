from flask import Flask, render_template, redirect, session, request, url_for
import db

app = Flask(__name__)
app.secret_key = "super"

'''DB_FILE="users.db"
db = sqlite3.connect(DB_FILE, check_same_thread=False)
c = db.cursor()'''

db.create_users_db()

'''
root route, renders the login page
'''
@app.route("/", methods=['GET', 'POST'])
def disp_loginpage():
    if 'username' in session: #home page rendered if there is a session
        return render_template('home.html', msg="successfully logged in")
    #return render_template('login.html')
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

    if db.valid_login(user, passw):
        session['username'] = user
        return render_template('home.html', msg = "successfully logged in")
    else:
        return render_template('login.html', msg="Login Failed")

'''
register route, allows user to create a new account
'''
@app.route("/register", methods=['GET','POST'])
def register_account():
    if 'username' in session: #if someone tries to register while already logged in
        return redirect(url_for('home'))

    if request.method == 'GET':
        return render_template('register.html')
    user = request.form['newUser']
    #user = request.form.get('newUser')
    passw = request.form['newPass']
    #passw = request.form.get('newPass')
    passw2 = request.form['confirmPass']

    if not passw == passw2: #checks if the password matches the confirmation password
        return render_template("register.html", FAILMSG="Passwords don't match!")
       
    if db.user_exists(user):
        return render_template('register.html', FAILMSG="Username is in use!")
    else:
        db.add_user(user, passw)
        return render_template('login.html', FAILMSG = "User registered!, Log in with your new credentials.")

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