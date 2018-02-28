from datetime import date

from flask import Flask
from flask import jsonify
from flask import current_app
from flask import render_template

from onelook.extensions import mongo_db

from onelook.utils.helpers import choice_movie_by_date



app = Flask(__name__,static_folder='templates')



@app.route('/')
def index():
    return render_template('index.html')



@app.route('/get_data')
def get_data():
    today = date.today()
    subject_id = choice_movie_by_date(today)
    item = mongo_db.movie.find_one({"subject_id":subject_id})
    return render_template('index.html',item=item)

