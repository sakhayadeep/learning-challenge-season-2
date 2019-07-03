from flask import Flask, render_template, request
app = Flask(__name__)

user = None
wrong_login = False

@app.route('/')
def home():
    return render_template('home.html', page_title = "Home", user = user)

@app.route('/loginPage')
def login():
    return render_template('loginForm.html', page_title = "Login", wrong_login = wrong_login)

@app.route('/login', methods=['POST'])
def do_login():
    global user
    global wrong_login
    POST_NAME = str(request.form['name'])
    POST_PASSWORD = str(request.form['password'])

    if(POST_PASSWORD == '123'):
        wrong_login = False
        user = POST_NAME
        return home()
    else:
        wrong_login = True
        return login()

@app.route('/register')
def register():
    return "under development"

@app.route('/logout')
def logout():
    global user 
    user = None
    return home()