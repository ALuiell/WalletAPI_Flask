from flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/hello/<name>')
def hello(name):
    return render_template('hello.html', name=name)


if __name__ == '__main__':
    app.run(debug=True)
