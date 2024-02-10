from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User, db
from werkzeug.security import generate_password_hash, check_password_hash

auth = Blueprint('auth',__name__) 

#this holds all the pages that the user can go to 

#login page
@auth.route('/login', methods =['GET','POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        user = User.query.filter_by(username = username).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category = 'success')
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password, try again.', category = 'error')
        else:
            flash('Username does not exist, try again.', category = 'error')

    return render_template("login.html", boolean = True)

#logout page
@auth.route('/logout')
def logout():
    return "<p>Logout</p>"

#signup page
@auth.route('/sign-up', methods =['GET','POST'])
def signup():
    if request.method == 'POST':
        username = request.form.get('username') #GETS the info from user input ans shoves in vars
        password = request.form.get('password')

        user = User.query.filter_by(username = username).first()

        #message flashing for future events will be comment it out with import flash
        #for example if(len(username)<4{flash('Please make a username greatuer then 4',category='error')})
        if user:
            flash('Username already exists', category = 'error')
        elif(len(username))<3:
            {flash('Please make a username greater then 3',category='error')}
        elif(len(password))<3:
            {flash('Please make a password greater then 3',category='error')}
        elif(len(password))>8:
            {flash('Please make a password less then 8',category='error')}
        elif(len(username))>8:
            {flash('Please make a username less then 8',category='error')}
        else:
            new_user = User(username = username, password = generate_password_hash(password, method='pbkdf2:sha256'))
            db.session.add(new_user)
            db.session.commit()
            flash('Account created!!!!',category='good')
            return redirect(url_for('views.home'))
    
    return render_template("sign_up.html")

#social page
@auth.route('/social')
def social():
    return "<p>Your friends here</p>"

#Profile page
@auth.route('/profile')
def profile():
    return "Your trophies and tasks"
