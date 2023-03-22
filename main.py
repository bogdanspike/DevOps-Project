from flask import Flask, render_template

app = Flask(__name__)


@app.route('/<name>')
def hello(name):
    # this condition should be something you query from db
    if name == "bobo":
        return {"bobo": "yes"}
    else:
        return render_template('index.html')


app.run()



