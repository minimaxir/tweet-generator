#!/usr/bin/python3

import yaml
import tweepy
import re
from textgenrnn import textgenrnn


def process_tweet_text(text):
    text = re.sub(r'http\S+', '', text)   # Remove URLs
    text = re.sub(r'@[a-zA-Z0-9_]+', '', text)  # Remove @ mentions
    text = text.strip(" ")   # Remove whitespace resulting from above
    text = re.sub(' +', ' ', text)   # Remove redundant spaces
    return text


with open("config.yml", "r") as f:
    cfg = yaml.load(f)

auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
auth.set_access_token(cfg['access_key'], cfg['access_secret'])

api = tweepy.API(auth)

texts = []
context_labels = []

for user in cfg['twitter_users']:
    all_tweets = tweepy.Cursor(api.user_timeline,
                               screen_name=user,
                               count=200,
                               tweet_mode='extended',
                               include_rts=False).pages(16)
    for page in all_tweets:
        for tweet in page:
            tweet_text = process_tweet_text(tweet.full_text)
            if tweet_text is not '':
                texts.append(tweet_text)
                context_labels.append(user)

textgen = textgenrnn()
textgen.train_on_texts(texts, context_labels, num_epochs=1)
textgen.save('{}_twitter_weights.hdf5'.format("_".join(cfg['twitter_users'])))
textgen.generate(20)
