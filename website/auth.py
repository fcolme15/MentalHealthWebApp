from flask import Blueprint 

auth = Blueprint('auth',__name__) 

#this holds all the pages that the user can go to 

#login page
@auth.route('/login')
def login():
    return "<p>Login</p>"

#logout page
@auth.route('/logout')
def logout():
    return "<p>Logout</p>"

#signup page
@auth.route('/sign-up')
def signup():
    return "<p>Sign Up</p>"

#social page
@auth.route('/social')
def social():
    return "<p>Your friends here</p>"
