#coding:utf-8
"""
Program: onelook
Description: onelook helper
Author: XY - mailyanxin@gmail.com
Date: 2018-02-28 10:51:33
Last modified: 2018-02-28 16:48:46
Python release: 3.4.3
"""

from onelook.extensions import mongo_db


def process_poster_img(subject_id):
    '''
    download local and rename
    '''
    pass

def choice_movie_by_date(date_obejct):
    '''
    param: date_object
    在分数8.0的池子里随机选
    return subject_id
    '''
    #选出一个
    m_movie = mongo_db.movie.find_one({'average': {"$gt":8.0}})
    if m_movie:
        subject_id = m_movie['subject_id']

        #mark
        date_str = date_obejct.strftime('%Y%m%d')
        mongo_db.movie.find_one_and_update(
                {'subject_id':subject_id},
                {"$set":{"dt_marked":date_str}}
                )
        return subject_id
    return None


