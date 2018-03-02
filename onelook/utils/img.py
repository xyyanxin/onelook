#coding:utf-8
""""
Program: onelook
Description: movie helper
Author: XY - mailyanxin@gmail.com
Date: 2018-03-01 11:05:17
Last modified: 2018-03-01 15:51:45
Python release: 3.4.3
"""
import os

from PIL import Image
from PIL import ImageFilter
from PIL import ImageDraw
from PIL import ImageFont

from flask import current_app

class Img(object):
    '''
    local origin img
    '''
    params = {
            'text_left_conner': 1,
            'text_top_conner': 1,
            'score_left_conner': 1,
            'score_top_conner': 1,
            'text_font_size': 10,
            'font_path': '/home/xy/workspace/onelook/onelook/templates/statics/fonts/XinH_CuJW.TTF',
            'font_size': 21,

            }
    def __init__(self,store_path):
        self.path = store_path

    def gauss_blur(self,radius=5):
        im = Image.open(self.path)
        im = im.filter(ImageFilter.GaussianBlur(radius=radius))
        im.save(self.path)

    def add_score(self,score):
        im = Image.open(self.path)
        draw = ImageDraw.Draw(im)
        font = ImageFont.truetype(Img.params['font_path'],Img.params['font_size'])
        draw.text((Img.params['text_left_conner'],Img.params['text_top_conner']),text=score,font=font,fill='black')
        im.save(self.path)

    def add_comment_title(self,comment_title):
        im = Image.open(self.path)
        draw = ImageDraw.Draw(im)
        font = ImageFont.truetype(Img.params['font_path'],Img.params['font_size'])
        draw.text((Img.params['text_left_conner'],Img.params['text_top_conner']),text=comment_title,font=font,fill='black')
        im.save(self.path)

    def get_font_path(self):
        font_path = os.path.join(current_app.root_path, 'templates','statics','fonts','XinH_CuJW.TTF')
        return font_path


if __name__ == '__main__':
    img = Img('/home/xy/workspace/onelook/onelook/templates/statics/poster_img/p2505314051.jpg')
    img.add_comment_title('im a comment title')
