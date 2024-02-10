#this holds all the pages that the user can go to 
from flask import Blueprint 

views = Blueprint('views',__name__) 

@views.route('/')#this will hold the main landing page
def home():
    return "<h1>Test</h1>"
