from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth',__name__) 

#this holds all the pages that the user can go to 

#login page
@auth.route('/login', methods =['GET','POST'])
def login():
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

        #message flashing for future events will be comment it out with import flash
        #for example if(len(username)<4{flash('Please make a username greatuer then 4',category='error')})
        if(len(username))<3:
            {flash('Please make a username greater then 3',category='error')}
        elif(len(password))<3:
            {flash('Please make a password greater then 3',category='error')}
        elif(len(password))>8:
            {flash('Please make a password less then 8',category='error')}
        elif(len(username))>8:
            {flash('Please make a username less then 8',category='error')}
        else:
            flash('Account created!!!!',category='good')

    
    return render_template("sign_up.html")

#social page
@auth.route('/social')
def social():
    return "<p>Your friends here</p>"

#Profile page
@auth.route('/profile')
def profile():
    return "<p>Your trophies and tasks/p>"
