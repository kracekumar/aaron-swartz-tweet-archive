#! -*- coding: utf-8 -*-

from archive import app
from flask.ext.sqlalchemy import SQLAlchemy
from datetime import datetime, time

db = SQLAlchemy(app)

class Tweet(db.Model):
    __tablename__ = 'tweet'
    id =  db.Column(db.Integer, primary_key=True)
    username = db.Column(db.UnicodeText, nullable=True)
    datetime =  db.Column(db.DateTime, nullable=False)
    status = db.Column(db.UnicodeText, nullable=False, default=u'')
    lang = db.Column(db.Unicode(5), nullable=False, default=u'en')
    image = db.Column(db.UnicodeText, nullable=False, default=u'')
    source = db.Column(db.UnicodeText, nullable=False, default=u'')
    location = db.Column(db.Unicode(50), nullable=True)
    latitude = db.Column(db.Numeric(8, 5), nullable=True)
    longitude = db.Column(db.Numeric(8, 5), nullable=True)
    hashtags = db.Column(db.UnicodeText, nullable=False, default=u'')
    urls = db.Column(db.UnicodeText, nullable=False, default=u'')
    user_mentions = db.Column(db.Unicode(150), nullable=True)
    media = db.Column(db.UnicodeText, nullable=True)

    def __init__(self, username, _date, _time, status, lang, image, source, location,
        latitude, longitude, hashtags, urls, user_mentions, media):
        self.username = username
        self.datetime = datetime.strptime(_date + ' ' + _time,'%m/%d/%Y %H:%M %p')
        self.status = status
        self.lang = lang
        self.image = image
        self.source = source
        self.location = location
        if len(latitude) > 8 or len(latitude) < 3:
            self.latitude = None
        else:
            try:
                self.latitude = latitude
            except: 
                self.latitude = None
        if len(longitude) > 8 or len(longitude) < 3:
            self.longitude = None
        else:
            try:
                self.longitude = longitude
            except:
                self.longitude = None
        self.hashtags = hashtags
        self.urls = urls
        self.user_mentions = user_mentions
        self.media = media
