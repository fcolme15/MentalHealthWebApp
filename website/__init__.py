from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'I LOVE UIC'

    from .views import views #imports the blueprints
    from .auth import auth 

    app.register_blueprint(views, url_prefix='/') #all urls are here in the blue print files
    app.register_blueprint(auth, url_prefix='/') #we can make a prefix so if you wanted to go to any page in the website you would fix the /something to add a prefix to any website url page

    return app
