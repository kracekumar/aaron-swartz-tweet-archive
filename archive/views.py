#! -*- coding: utf-8 -*-

from archive import app
from archive.models import Tweet, db
from flask import render_template
from sqlalchemy import func
from pytz import utc
import operator


EXCLUDE = set(["a", "an", "the", "death", "aaron", "swartz", "tweet", "of", "in",
 u"swartz\u2019s", "that", "cause", "and", "or", "to", "for", '-', 'swartz', 'on',
 "swartz's", "#aaronswartz", "swartz’s", "swartz,", "swartz:", "we", "as", "than",
 "by", "us", "at", "free", "is", "was"])


def build_long_sentence():
    tweets = Tweet.query.order_by(Tweet.datetime.desc()).all()
    text = ""
    return text.join([tweet.status for tweet in tweets])


def most_used_words(sentence, exclude):
    words_times = {}
    for word in sentence.split():
        word = word.lower()
        if word not in exclude and not word.startswith('http') and not word.startswith('@'):
            if word in words_times:
                words_times[word] += 1
            else:
                words_times[word] = 1
    return words_times


@app.template_filter('fulldate')
def fulldate(date):
    return utc.localize(date).astimezone('UTC').strftime("%a, %b %e %H:%M %p")


@app.route('/')
def index():
    tweets = Tweet.query.order_by(Tweet.datetime.desc()).all()
    return render_template('index.html', tweets=tweets)


@app.route('/graphs')
def graphs():
    results = db.session.query(Tweet.datetime, func.count(Tweet.datetime)).group_by(Tweet.datetime).all()
    return render_template('graphs.html', results=results)


@app.route('/analysis')
def analysis():
    sentence = build_long_sentence()
    words = most_used_words(sentence, EXCLUDE)
    return render_template('analysis.html', words=sorted(words.iteritems(), key=operator.itemgetter(1), reverse=True)[:50])