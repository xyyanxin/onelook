#coding:utf-8
"""
Program: onelook
Description: onelook helper
Author: XY - mailyanxin@gmail.com
Date: 2018-02-28 10:51:33
Last modified: 2018-03-02 10:27:34
Python release: 3.4.3
"""
import os
import requests
from datetime import date
from flask import current_app

def get_url_suffix(object):
    if isinstance(object,str): return os.path.splitext(object)[1]
    return None

def get_url_name(url):
    full_name = os.path.basename(url)
    return full_name

def download_img(store_path,url):
    url = url.replace(
            'https://img3.doubanio.com/view/photo/sqxs',
            'https://img3.doubanio.com/view/photo/l',
            )
    current_app.logger.info('download picture : %s'%url)
    r = requests.get(url)
    with open(store_path,'wb') as f:
        img = r.content
        f.write(img)


def get_today_str():
    today = date.today()
    return today.strftime('%Y%m%d')

