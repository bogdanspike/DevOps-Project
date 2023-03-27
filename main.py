import psycopg2
from db_connection import names
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hi():
    return 'hi'


@app.route('/<name>')
def hello(name):
    # this condition should be something you query from db
    if name in names:
        return {"bobo": "yes"}
    else:
        return render_template('index.html')


if __name__ == '__main__':
    app.run()
