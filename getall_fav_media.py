#coding: UTF-8
from requests_oauthlib import OAuth1Session
from datetime import datetime
import urllib2
import json
import token
from download_twitter_media import *
import time
import os.path
import sys
import sqlite3

dl_dir = 'media/'

dbname = 'twitter.db'
conn = sqlite3.connect(dbname)
c = conn.cursor()

import re

twitter = OAuth1Session(token.CONSUMER_KEY, token.CONSUMER_SECRET, token.ACCESS_TOKEN, token.ACCESS_TOKEN_SECRET)

i = 0
max_id = ''
min_id = ''
while True:
  params = {"count": 180, "include_entities": True}
  if max_id != '':
    if max_id == min_id:
      break
    params["max_id"] = long(min_id) - 1
  req = twitter.get("https://api.twitter.com/1.1/favorites/list.json", params = params)
  likes = json.loads(req.text)
  if len(likes) == 0:
      print 'DONE.'
      break
  with open('test.txt', "a") as fout:
    json.dump(likes, fout, indent=2)
  max_id = likes[0]['id_str']
  min_id = likes[len(likes)-1]['id_str']
  print 'i:'+str(i), min_id, max_id

  for like in likes:
    for url in retrieve(like):
      root, ext = os.path.splitext(url[2])
      c.execute("select * from likes where tweet_id=?", [url[0]])
      l = c.fetchall()
      if len(l) == 0:
        sql = 'insert into likes (tweet_id, created_at) values (?,?)'
        dl(url[2], dl_dir+url[0]+ext)
        c.execute(sql, (url[0], datetime.now().strftime('%Y/%m/%d %H:%M:%S')))
        print url[0]
        conn.commit()
  i = i + 1
  time.sleep(5*60)
