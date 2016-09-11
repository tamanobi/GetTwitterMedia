#coding: UTF-8
from twitter import *
import os.path
import token
import json
from download_twitter_media.py import *

dl_dir = 'trigger/'
auth = OAuth(token.ACCESS_TOKEN, token.ACCESS_TOKEN_SECRET, token.CONSUMER_KEY, token.CONSUMER_SECRET)

twitter_stream = TwitterStream(auth=auth, domain="userstream.twitter.com")
for msg in twitter_stream.user():
    with open('user_activity.json', "a") as fout:
        if msg.has_key('event') and msg['event'] == 'favorite':
            for url in retrieve(msg['target_object']):
                root, ext = os.path.splitext(url[2])
                dl(url[2], dl_dir+url[0]+ext)
                json.dump(msg, fout, indent=2)

