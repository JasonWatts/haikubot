#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
import tweepy, time, sys
from random import randint
 
#enter the corresponding information from your Twitter application:
CONSUMER_KEY = 'VGf9KuoNn9oWB5rn8cgQ7712x'#keep the quotes, replace this with your consumer key
CONSUMER_SECRET = 'wJsYQxdD2BdJrhD6ndti8NFPG4UCxhQSE68PcFhU4R0UNhnIi7'#keep the quotes, replace this with your consumer secret key
ACCESS_KEY = '952646059661996032-UgwFKEs8Kv8YTHogegvNTeoGlVZsQ9U'#keep the quotes, replace this with your access token
ACCESS_SECRET = '1C598OymNsTNw37UKD8cJImVY2is7yO2IeikfvdBs5UEx'#keep the quotes, replace this with your access token secret
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)
 
filename=open('1syllable.txt','r')
f=filename.readlines()
filename.close()

wordList1 = ["enchanting", "amazing", "colourful", "delightful", "honeydew", "delicate","shimmering", "fantastic","luminous", "ladybug", "butterfly", "happiness","blueberry","hydroflask", "burrito"]
wordList2 = ["visions", "distance", "conscience", "process", "chaos","holy", "chubby","humor","grapefruit","idle","item","label","bunny","woman","birthday","frisky","nuisance","fire","water", "eyebrow","nostril","peanut"
,"lady","legal","locate","major","minus","moment","motor","music","nation","notion","obey","odor","oval",
"paper","photo","pilot","pony","pretend","private","pupil","radar","razor","reason","recess","regard","resist","rival","robot","rotate","rumor","secret","silent","siren","soda"]
wordList3 = ["superstitious", "contradicting", "overwhelming","undermining", "intermittent", "malificent", "eternity"]
wordList4 = ["true", "dark", "cold", "warm", "great", "a", "all", "and", "are", "as", "be", "by", "day", 
"did", "each", "few", "for", "get", "have", "he", "him", "his", "i", "in", "is", "it","long","man"
,"me","more","much","my","new","not","now","of","off","old","one","on","or","out","same","she","so","state","then","that","they","then","time","to","up","war","was"]
wordList5 = ["visions", "distance", "conscience", "process", "chaos","holy","humor","idle","item","label"
,"lady","legal","locate","major","minus","moment","motor","music","nation","notion","obey","odor","oval",
"paper","photo","pilot","pony","pretend","private","pupil","radar","razor","reason","recess","regard","resist","rival","robot","rotate","rumor","secret","silent","siren","soda"]
wordList6 = ["beautiful", "imperfect", "subtley"]
wordList7 = ["visions", "distance", "conscience", "process", "chaos","holy","humor","idle","item","label"
,"lady","legal","locate","major","minus","moment","motor","music","nation","notion","obey","odor","oval",
"paper","photo","pilot","pony","pretend","private","pupil","radar","razor","reason","recess","regard","resist","rival","robot","rotate","rumor","secret","silent","siren","soda"]

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