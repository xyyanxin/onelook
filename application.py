from flask import Flask
from flask import render_template
app = Flask(__name__,static_folder='templates')

@app.route('/')
def hello_world():
    #return 'Hello, World!'
    return render_template('start.html')


if __name__ == '__main__':
    app.run('host=127.0.0.1:5000')
