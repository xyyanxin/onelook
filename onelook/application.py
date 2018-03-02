#coding:utf-8
""""
Program: onelook
Description: app
Author: XY - mailyanxin@gmail.com
Date: 2018-03-02 11:55:15
Last modified: 2018-03-02 11:57:47
Python release: 3.4.3
"""
import os
from datetime import date

from flask import Flask
from flask import jsonify
from flask import current_app
from flask import render_template

from onelook.extensions import mongo_db
from onelook.utils.movie import Movie



app = Flask(__name__,static_folder='templates')
app.config['DEBUG'] = True
app.config['poster_path'] = os.path.join(current_app.root_path,'templates','statics', 'poster_img')
app.config['font_path'] = os.path.join(current_app.root_path, 'templates','statics','fonts','XinH_CuJW.TTF')

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/get_data')
def get_data():
    # 一天一影
    the_movie = Movie(date.today())

    item = {}
    item['subject_id'] = the_movie.subject_id
    item['name'] = the_movie.name
    item['comment_title'] = the_movie.comment_title
    item['img_store_path'] = the_movie.poster_store_path

    return render_template('index.html',item=item)
