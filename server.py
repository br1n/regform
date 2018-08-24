from flask import Flask, render_template, redirect, request, session, flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
app.secret_key = "henlobilo"


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/register', methods = ['POST'])
def register():
    form = request.form 
    passFlag = True

    session['email'] = form['email']
    session['first_name'] = form['first_name']
    session['last_name'] = form['last_name']
    session['password'] = form['password']
    session['confirm_password'] = form['confirm_password']
    session['form'] = request.form

    #First name vaildation
    if len(form['first_name']) < 1:
        flash('Invalid first name')
        passFlag = False
    elif not form['first_name'].isalpha():
        flash('First and Last Name cannot contain any numbers')
        passFlag = False
    
    #Last name validation
    if len(form['last_name']) < 1:
        flash('Invalid first name')
        passFlag = False
    elif not form['last_name'].isalpha():
        flash('First and Last Name cannot contain any numbers')
        passFlag = False

    #email validation
    if len(form['email']) < 1:
        flash('Invalid email')
        passFlag = False
    elif not EMAIL_REGEX.match(form['email']):
        flash('Invalid email')
        passFlag = False

    #password validation
    if len(form['password']) < 6:
        flash('Password must contain at least 6 characters')
        passFlag = False
    elif form['password'] != form['confirm_password']:
        flash('Passwords do not match')
        passFlag = False
    
    #If all fields correct
    if passFlag == True:
        flash('Thank you for submitting your information!')
    return redirect('/')

app.run(debug=True)
    


   