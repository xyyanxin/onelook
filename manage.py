#coding:utf-8
""""
Program: onelook
Description: manager
Author: XY - mailyanxin@gmail.com
Date: 2018-02-28 11:07:18
Last modified: 2018-02-28 11:15:41
Python release: 3.4.3
"""

from flask_script import Manager
from flask_script import prompt_bool

from onelook.application import app

manager = Manager(app)

@manager.command
def initdb():
    if prompt_bool("Are you sure? You will init your database"):
        print('hello')
        pass


if __name__ == '__main__':
    manager.run()
