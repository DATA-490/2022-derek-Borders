import argparse
import sys
import praw
import prawcore
import shutil
import subprocess
import os
import errno
import re
import cv2
import numpy as np
from math import ceil
import urllib.request
from PIL import Image

reddit = praw.Reddit( \
    client_id='VZDFQR1wT8giqAVcq09UmQ', \
    client_secret='27AnuMqvvV6CbxekJspgAyxD4UYThw', \
    user_agent='nms-screenshot-scraper', \
    username='nms_cartographer', \
    password='y1C1FMt2X9mu')

nmsce = reddit.subreddit('NMSCoordinateExchange')

def gallery_first_image(gallery_url):
    """Gets first image from a reddit gallery post
    """

    try:
        submission = reddit.submission(url = gallery_url)
        image_dict = submission.media_metadata
        # return re.sub('width=[0-9]+', 'width=1920', list(image_dict.values())[0]['s']['u'])
        return list(image_dict.values())[0]['s']['u']
    except: 
        return ""

def url_to_img(url):
    """Use pillow to create a pillow.image object from a url
    """

    ext = url.split(".")[-1].split("?")[0]
    temp = "temp." + ext
    urllib.request.urlretrieve(url, temp)
    return Image.open(temp)

class post_info():
    """ Simple class holding a subset of 'PRAW.submission' attributes 
    """

    def __init__(self, post, flair_text):
        self.post_id = post.id
        self.title = post.title
        try:
            self.author_id = post.author.id
            # self.author_name = post.author.name
        except:            
            self.author_id = "-1"
            self.author_name = "deleted"
        # self.upvotes = post.score
        self.flair_text = flair_text
        # self.flair_text = post.link_flair_text
        self.url = post.url
        self.address = "000000000000"
        self.planet_index = -1
        self.system_index = -1
        self.coord_y =-1
        self.coord_x =-1
        self.coord_z =-1
        
    def process_address(self, model):
        """Extracts string address and numeric coordinates from post image
        
        Processes image, crops address, classifies runes, extracts address string, populates coords
        """
        # Get image
        try:
            if self.url.split("/")[-2] == "gallery":
                self.url = gallery_first_image(self.url)
        except:
            self.url = ""
        # Preprocess
        # For each glyph
            # classify glyph using model
            # append character to address string
        if "u" in self.address: 
            self.address = ""
            return
        # Convert hex strings to decimal, store as numeric addresses
        self.planet_index   = int(self.address[0], 16)
        self.system_index   = int(self.address[1:4], 16)
        self.coord_y        = int(self.address[4:6], 16)
        self.coord_x        = int(self.address[6:9], 16)
        self.coord_z        = int(self.address[9:], 16)

    def to_dict(self):
        """Extracts attributes to dictionary
        """
        return {
            'post_id': self.post_id,
            # 'title': self.title,
            'author_id': self.author_id,
            # 'author_name': self.author_name,
            # 'upvotes': self.upvotes,
            'flair_text': self.flair_text,
            'subject' : self.flair_text.split("/")[0],
            'galaxy' : self.flair_text.split("/")[1],
            'update' : self.flair_text.split("/")[2],
            'url': self.url,            
            'address': self.address,
            'body_index_h': int(self.address[0], 16), # Convert from hex string to integer value
            'sys_index_h': int(self.address[1:4], 16),
            'region_y_h': int(self.address[4:6], 16),
            'region_z_h': int(self.address[6:9], 16),
            'region_x_h': int(self.address[9:], 16) 
        }



