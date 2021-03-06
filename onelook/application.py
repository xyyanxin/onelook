#coding:utf-8
""""
Program: onelook
Description: app
Author: XY - mailyanxin@gmail.com
Date: 2018-03-02 11:55:15
Last modified: 2018-03-06 15:34:30
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


@app.route('/')
def index():
    # 一天一影
    the_movie = Movie(date.today())

    item = {}
    item['subject_id'] = the_movie.subject_id
    item['name'] = the_movie.name
    item['comment_title'] = the_movie.comment_title
    item['img_store_path'] = the_movie.poster_store_path
    item['thunder_url'] = the_movie.thunder_url
    item['average'] = the_movie.average

    return render_template('index_all_photo.html',item=item)
