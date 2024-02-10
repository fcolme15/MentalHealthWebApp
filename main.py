from website import create_app

app = create_app()

if __name__ == '__main__': #only runs when is run off the file directally
    app.run(debug = True) #runs flask app everytime change is made it auto runs the server turn off when in production
    