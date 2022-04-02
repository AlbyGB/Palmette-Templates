'''
First make sure to run 'pip install -r requirements.txt'
Docs for Pandas module: https://flask.palletsprojects.com/en/latest/
'''
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

app.run(debug=True)