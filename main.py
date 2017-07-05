from flask import Flask, request, redirect,render_template
app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return render_template('index.html')

def PWD_USR_Valid(user_input):
    if len(user_input) < 4 or len(user_input) > 20 or ' ' in user_input:
        return False

def Email_Vaid(Email_input):
    if PWD_USR_Valid(Email_input) or '@' not in Email_input:
        return False
    
@app.route('/signup', methods=['POST','GET'])
def welcome():
    username = request.form['username']
    email = request.form['email']
    password = request.form['password']
    verify_password = request.form['verify_password']

    if PWD_USR_Valid(username) == False:
        error_username = "Enter a vaild username"
        return render_template('index.html', error_username=error_username, username=username, email=email)
    
    if len(email) >= 1:
        if Email_Vaid(email) == False:
            error_email = "Enter a vaild email"
            return render_template('index.html', error_email=error_email, username=username, email=email)

    return render_template('welcome.html', username=username)


app.run()