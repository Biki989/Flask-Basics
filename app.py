from flask import Flask

## WSGI application
app=Flask(__name__)

@app.route("/")
def welcome():
    return "welcome to this course"
@app.route("/index")
def index():
    return "This is index page"

if __name__== '__main__':
    app.run(debug=True)