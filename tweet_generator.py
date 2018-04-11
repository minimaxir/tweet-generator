#!/usr/bin/python3

import yaml
import tweepy
import re
# from textgenrnn import textgenrnn


with open("config.yaml", "r") as f:
    cfg = yaml.load(f)

# textgen = textgenrnn()


auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
auth.set_access_token(cfg['access_key'], cfg['access_secret'])

api = tweepy.API(auth)

for user in cfg['twitter_users']:
    i = 0
    all_tweets = tweepy.Cursor(api.user_timeline,
                               screen_name=user,
                               count=200,
                               tweet_mode='extended',
                               include_rts=False).pages(16)
    for page in all_tweets:
        for tweet in page:
            print(process_tweet_text(tweet.full_text))
            i += 1
            print(i)


def process_tweet_text(text):
    text = re.sub(r'http\S+', '', text)   # Remove URLs
    text = re.sub(r'@[a-zA-Z0-9_]+', '', text)  # Remove @ mentions
    text = text.strip(" ")   # Remove whitespace resulting from above
    return text
