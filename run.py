from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hola, Welcome to this chicken spot!!</h1>'

@app.route('/test')
def test():
    return 'This is a test!'