from flask import Flask    #from the flask module import the Flask class


app = Flask(__name__)       # we are instantiating our Flask class into our app variable.

#when people request "/", call the function index
@app.route("/")             # A decorator that creates a new HTTP path.
def index():                # In the context of flask, this is a view function.
    return "<h1>Hello, world!</h1>"     #return statement

@app.route("/users/shane")
def about_shane():
    me={
        "first_name":"Shane",
        "last_name":"Dixon",
        "hobbies":"Outdoor Activities",
        "active":True
    }
    return me  #flask automatically converts to JSON

@app.route("/greeting/<name>")
def print_name(name):
    return "<h1>Hello, %s!</h1>" % name  # %s tells it to format as a string and the string can be found after the %


@app.route("/square/<int:num>")
def square_num(num):
    return "<h1>That number, squared, is: %s</h1>" % (num**2)