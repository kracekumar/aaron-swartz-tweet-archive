#! -*- coding: utf-8 -*-

from archive import app
from archive.models import db, Tweet
import csv
import os
import sys


def load_db(filename='Aaron_tweets.csv'):
    if os.path.exists(filename):
        with open(filename) as f:
            csv_reader = list(csv.reader(f))[1:]
            for item in csv_reader:
                tweet = Tweet(*item[1:])
                db.session.add(tweet)
            db.session.commit()
            print("Added %d tweets to db" % (len(csv_reader)))
    else:
        print("Filename: %s doesn't exist." % (filename))
        sys.exit()


if __name__ == "__main__":
    db.create_all()
    if len(sys.argv) >= 2:
        load_db(sys.argv[1])
    else:
        load_db()
