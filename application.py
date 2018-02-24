from flask import Flask
from flask import render_template
app = Flask(__name__,static_folder='templates')

@app.route('/')
def hello_world():
    #return 'Hello, World!'
    return render_template('start.html')
