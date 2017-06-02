#!/usr/bin/python
# -*- coding: utf-8 -*-
import tweepy
import json
import telegram
import time

consumer_key = 'ETijATNvEtYneYS68eYKixs5S'
consumer_secret = 'KGkf7Zqny4HtFZrLSUwJEdJXVRGF6uu1T9DQaoba5Ac8RljbtT'
access_token = '2871687840-Gp0JTqhqn19yvat7SAslLgAPDYEgXoScwqukRm2'
access_token_secret = 'AsrdusBscWazDV0F04bXXajm4xi4Nz9ZzjVE7eBvVBxWY'
# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
location = api.trends_closest(43.9072092,-69.9611376)

WOEID = location[0]['woeid']
trends = api.trends_place(WOEID)



'''
for i in range(len(trends1[0]['trends'])):
	print trends1[0]['trends'][i]
	print ('\n')
'''

