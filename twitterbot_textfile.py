# Import our Twitter credentials from credentials.py
import tweepy
import random
from time import sleep
from credentials import *

# Access and authorize our Twitter credentials from credentials.py
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

choicefile=open("JapaneseWords.txt","r", encoding='utf-8-sig')
linelist=[]
for line in choicefile:
    try:
        unicode_text = choicefile.decode('UTF-8')
        linelist.append(line)
        choice=random.choice(linelist)
        print(choice)
        
        if line != '\n':
            api.update_status(line)
        else:
            pass
    except tweepy.TweepError as e:
        print(e.reason)
        
# Add sleep method to space tweets by 5 seconds each
    sleep(20)