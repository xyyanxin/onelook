from flask import Flask
from flask import jsonify
from flask import current_app
from flask import render_template

from onelook.extensions import db

app = Flask(__name__,static_folder='templates')


@app.route('/')
def index():
    return render_template('start.html')

@app.route('/get_data')
def get_data():
    movie = db.douban.movie
    item = movie.find_one()
    return render_template('start.html',item=item)

if __name__ == '__main__':
    app.run()
