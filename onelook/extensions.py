#coding:utf-8
""""
Program: onelook
Description: extensions
Author: XY - mailyanxin@gmail.com
Date: 2018-02-28 10:57:59
Last modified: 2018-02-28 16:47:01
Python release: 3.4.3
"""

from pymongo import MongoClient
from flask_sqlalchemy import SQLAlchemy

# mongo
mongo_db = MongoClient('127.0.0.1',27017)
mongo_db = mongo_db.douban

# mysql
mysql_db = SQLAlchemy()

pass
