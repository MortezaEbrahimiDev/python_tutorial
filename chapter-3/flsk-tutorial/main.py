from flask import Flask

app=Flask(__name__)

@app.route("/hello")
def hello_world():
    return '<h1>Hello world!</h1>'


@app.route('/')
def index():
    return 'welcome to my site'

@app.route('/post/<int:id>')
def post(id):
    return f'posted is:{id}'

@app.route('/user/<username>')
def say_hello(username):
    return f'hello {username}'