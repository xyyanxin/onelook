#coding:utf-8
""""
Program: onelook
Description: movie helper
Author: XY - mailyanxin@gmail.com
Date: 2018-03-01 11:05:17
Last modified: 2018-03-05 11:51:25
Python release: 3.4.3
"""
import os
import requests

from flask import current_app
from onelook.extensions import mongo_db
from .helpers import get_url_name,get_url_suffix, download_img,get_today_str
from .img import Img


class Movie(object):

    def __init__(self,date_obejct):
        the_movie = Movie.one_day_one_movie(date_obejct)
        if the_movie.get('dt_view',None) is None:
            Movie.process_poster_image(the_movie['subject_id'])
            Movie.update_dt_view(the_movie['subject_id'])

        self.subject_id = the_movie['subject_id']
        self.name = the_movie['name']
        self.image_detail = the_movie['image_detail']
        self.comment_title = the_movie['comment_title']
        self.thunder_url = the_movie.get('thunder_url','管理员太他妈懒，还没有添加迅雷链接')
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
        筛出海报照片
        下载
        美化
        '''
        the_movie = Movie.query_movie(subject_id)
        url_list = Movie.filter_poster_url(subject_id)
        for index,url in enumerate(url_list):
            img_name = get_url_name(url)
            poster_path = os.path.join( current_app.root_path, \
                    'templates','statics', 'poster_img', \
                    '{img_name}'.format(img_name=img_name))
            download_img(poster_path,url)
            img = Img(poster_path)
            img.reset_size()
            if index == 0:
                # 对首张图片进行模糊并加入文字
                img.gauss_blur(1)
                img.add_score('<<{0}>>|豆瓣评分:{1}'.format(the_movie['name'],the_movie['average']))
                comment_title = '\n'.join(the_movie['comment_title'])
                img.add_comment_title(comment_title)
            # 加入logo
            img.add_logo()


    @staticmethod
    def filter_poster_url(subject_id,num=6):
        '''
        筛选有效的海报链接
        选出6个
        '''
        current_app.logger.info(subject_id)
        the_movie = mongo_db.movie.find_one({'subject_id': subject_id})
        url_list = the_movie['image_detail']
        if len(url_list) <= num: return url_list

        ret = []
        for url in url_list:
            suffix = get_url_suffix(url)
            if url.startswith('https://img3') and suffix in {'.webp', '.jpg', '.png'}:
                ret.append(url)
        return ret[:6]

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

    @staticmethod
    def query_movie(subject_id):
        the_movie = mongo_db.movie.find_one({'subject_id': subject_id})
        return the_movie
