from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path

db = SQLAlchemy()
DB_Name = "database.db"

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'I LOVE UIC'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_Name}'
    db.init_app(app)#takes data base and tells its gunna use the app 
    #SQL TIME BABYYYYY I LOVE SQL 341!!!

    from .views import views #imports the blueprints
    from .auth import auth 

    app.register_blueprint(views, url_prefix='/') #all urls are here in the blue print files
    app.register_blueprint(auth, url_prefix='/') #we can make a prefix so if you wanted to go to any page in the website you would fix the /something to add a prefix to any website url page

    from .models import User########, Note #loads the modles to make sure it defigns the classes in the table'

    #create_database(app)
    with app.app_context():
        db.create_all()
        print('Created Database!')

    return app

#def create_database(app):
#    if not path.exists('website/' + DB_Name):
#        db.create_all(app=app) #1:33:44 error when creating the fucking table 
#        print('Created Database!')
