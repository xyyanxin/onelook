#coding:utf-8
""""
Program: onelook
Description: movie helper
Author: XY - mailyanxin@gmail.com
Date: 2018-03-01 11:05:17
Last modified: 2018-03-01 14:22:43
Python release: 3.4.3
"""
import os
import requests

from flask import current_app
from onelook.extensions import mongo_db
from .helpers import get_url_name,get_url_suffix, download_img,get_today_str


class Movie(object):

    def __init__(self,date_obejct):
        the_movie = Movie.one_day_one_movie(date_obejct)
        current_app.logger.info(the_movie['subject_id'])
        if the_movie.get('dt_view',None) is None:
            Movie.process_poster_image(the_movie['subject_id'])
            Movie.update_dt_view(the_movie['subject_id'])

        self.subject_id = the_movie['subject_id']
        self.name = the_movie['name']
        self.image_detail = the_movie['image_detail']
        self.comment_title = the_movie['comment_title']
        self.poster_store_path = Movie.get_poster_store_path(self.subject_id)


    @staticmethod
    def one_day_one_movie(date_obejct):
        '''
        param: date_object
        在分数8.0的池子里随机选
        return subject_id
        '''
        date_str = date_obejct.strftime('%Y%m%d')
        m_movie = mongo_db.movie.find_one({'average': {"$gt":8.0},'dt_view':date_str})

        if not m_movie:
            m_movie = mongo_db.movie.find_one(
                    {'$and': [
                        {'average':{'$gt':8.0}},
                        {'dt_view':{'$exists':False}}]})

        return m_movie


    @staticmethod
    def process_poster_image(subject_id):
        '''
        筛出海报照片并下载
        '''
        url_list = Movie.filter_poster_url(subject_id)
        ret = []
        for url in url_list:
            img_name = get_url_name(url)
            poster_path = os.path.join( current_app.root_path, \
                    'templates','statics', 'poster_img', \
                    '{img_name}'.format(img_name=img_name))
            download_img(poster_path,url)


    @staticmethod
    def filter_poster_url(subject_id,num=6):
        '''
        筛选有效的海报链接
        选出6个
        '''
        current_app.logger.info(subject_id)
        the_movie = mongo_db.movie.find_one({'subject_id': subject_id})
        current_app.logger.info(the_movie)
        url_list = the_movie['image_detail']
        if len(url_list) <= num: return url_list

        ret = []
        for url in url_list:
            suffix = get_url_suffix(url)
            if url.startswith('https://img3') and suffix in {'.webp', '.jpg', '.png'}:
                ret.append(url)
            if len(ret) == num:return ret

    @staticmethod
    def get_poster_store_path(subject_id):
        url_list = Movie.filter_poster_url(subject_id)
        ret = []
        for url in url_list:
            img_name = get_url_name(url)
            store_path = os.path.join(
                    'templates','statics','poster_img','{0}'.format(img_name)
                    )
            ret.append(store_path)
        return ret

    @staticmethod
    def update_dt_view(subject_id):
        mongo_db.movie.find_one_and_update(
                {'subject_id':subject_id},
                {"$set":{"dt_view":get_today_str()}}
                )
