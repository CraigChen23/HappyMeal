from flask import Flask, render_template, redirect, session, request, url_for
import json
import db
import api_functions as api 
from db import get_country_data, get_years, get_years_data

app = Flask(__name__)
app.secret_key = "super"

'''DB_FILE="users.db"
db = sqlite3.connect(DB_FILE, check_same_thread=False)
c = db.cursor()'''

db.create_users_db()
db.create_exports_db()
db.populate_exports_db()

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

@app.route("/home", methods=['GET', 'POST'])
def home():
    return render_template('home.html', data = get_years_data(1990))

'''
# allow user to search country info and it brings to page with info
@app.route("/search/<input>", methods=['GET', 'POST'])
def get_country_info(input):
    if not 'username' in session: #if someone tries to go here when not logged in
        return redirect(url_for('login'))

    if request.method == 'POST':
        if 'input' in request.form: #if user
            user_search = request.form['country_name']
            if len(user_search) > 0: # checks if the input is blank
                return redirect(url_for("search_results", input = user_search))

    #country_name = request.form.get("country_name")
    return render_template('chart.html', country = country_name)
'''

@app.route("/home/search", methods=['GET', 'POST'])
def get_database_info():
    if not 'username' in session: #if someone tries to go here when not logged in
        return redirect(url_for('login'))

    if request.method == 'POST':
        country_name = request.form.get("country_name")
    #print("The years in the data are: " + str((get_years()[1:])))
    #print("Data from " + country_name + ": " +  str(get_country_data(country_name)))
    return render_template('linechart.html', country = country_name, xvalue = get_years()[1:], yvalue = get_country_data(country_name))

'''
#click on country and it brings you to a page with all their info
@app.route("/countryinfo", methods=['GET', 'POST'])
def get_country_info():
    data = request.get_json() # retrieve the data sent from JavaScript
    # process the data using Python code
    result = data['title']
    return jsonify(result=result)
    return render_template('chart.html')
'''

@app.errorhandler(500)
def no_info():
    return render_template('noinfo.html'), 500
#================================================#

if __name__ == "__main__":  # true if this file NOT imported
    app.debug = True        # enable auto-reload upon code change
    app.run(host = '0.0.0.0')