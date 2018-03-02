#coding:utf-8
""""
Program: onelook
Description: movie helper
Author: XY - mailyanxin@gmail.com
Date: 2018-03-01 11:05:17
Last modified: 2018-03-02 14:34:06
Python release: 3.4.3
"""
import os

from PIL import Image
from PIL import ImageFilter
from PIL import ImageDraw
from PIL import ImageFont

from flask import current_app
from .helpers import get_font_path

class Img(object):
    '''
    local origin img
    '''
    params = {
            'text_left_conner': 20,
            'text_top_conner': 550,
            'score_left_conner': 100,
            'score_top_conner': 300,
            'logo_left_conner': 430,
            'logo_top_conner': 770,
            'text_font_size': 15,
            'score_font_size': 35,
            'logo_font_size': 20,
            'img_width': 800,
            'img_height': 800,
            'logo_text': 'byonelook.com|每天一部豆瓣高分|by xy.'
            }
    def __init__(self,store_path):
        self.path = store_path

    def gauss_blur(self,radius=3):
        im = Image.open(self.path)
        im = im.filter(ImageFilter.GaussianBlur(radius=radius))
        im.save(self.path)

    def add_score(self,score):
        im = Image.open(self.path)
        draw = ImageDraw.Draw(im)
        font = ImageFont.truetype(os.path.join(current_app.root_path,'templates','statics','fonts','XinH_CuJW.TTF'),Img.params['score_font_size'])
        draw.text((Img.params['score_left_conner'],Img.params['score_top_conner']),text=score,font=font,fill='black')
        im.save(self.path)

    def add_comment_title(self,comment_title):
        im = Image.open(self.path)
        draw = ImageDraw.Draw(im)
        font = ImageFont.truetype(os.path.join(current_app.root_path,'templates','statics','fonts','XinH_CuJW.TTF'),Img.params['text_font_size'])
        draw.text((Img.params['text_left_conner'],Img.params['text_top_conner']),text=comment_title,font=font,fill='black')
        im.save(self.path)


    def reset_size(self):
        im = Image.open(self.path)
        # 按比例缩放
        im = im.resize((Img.params['img_width'],Img.params['img_height']))
        # or 抠图然后缩放
        #origin_size = im.size
        #im = im.crop((
        #    origin_size[0]/2 - Img.params['img_width']/2,
        #    origin_size[1]/2 - Img.params['img_height']/2,
        #    origin_size[0]/2 + Img.params['img_width']/2,
        #    origin_size[1]/2 + Img.params['img_height']/2,
        #    ))
        im.save(self.path)

    def add_logo(self):
        im = Image.open(self.path)
        draw = ImageDraw.Draw(im)
        font = ImageFont.truetype(os.path.join(current_app.root_path,'templates','statics','fonts','XinH_CuJW.TTF'),Img.params['logo_font_size'])
        draw.text((Img.params['logo_left_conner'],Img.params['logo_top_conner']),text=Img.params['logo_text'],font=font,fill='black')
        im.save(self.path)



if __name__ == '__main__':
    img = Img('/home/xy/workspace/onelook/onelook/templates/statics/poster_img/p2410383586.jpg')
    img.reset_size()
