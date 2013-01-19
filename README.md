Internet Archive have gathered all the tweets about @aaronsw after his death. Lets build a nice web interface to it.

http://archive.org/details/AaronTweets

Innstall deps:
------

`sudo pip install -r requirements.txt`

Add all tweets to db
-------------

`python migrate.py`

Run server
---------
`python runserver.py`

visit `http://localhost:3333`
