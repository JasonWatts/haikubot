#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
import tweepy, time, sys
from random import randint
from config import *    #CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET
from wordLists import *

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

wordIndex1=randint(0, len(wordList1)-1)
wordIndex2=randint(0, len(wordList2)-1)
wordIndex3=randint(0, len(wordList3)-1)
wordIndex4=randint(0, len(wordList4)-1)
wordIndex5=randint(0, len(wordList5)-1)
wordIndex6=randint(0, len(wordList6)-1)
wordIndex7=randint(0, len(wordList7)-1)

haiku = wordList1[wordIndex1] + " " + wordList2[wordIndex2] + ",\n"
haiku = haiku + wordList3[wordIndex3] + " " + wordList4[wordIndex4] + " " + wordList2[wordIndex5]  + ",\n"
haiku = haiku + wordList6[wordIndex6] + " " + wordList2[wordIndex7] + "."

print(haiku)

api.update_status(haiku)
time.sleep(1)      