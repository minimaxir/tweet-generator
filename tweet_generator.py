#!/usr/bin/python3

import yaml
import tweepy
import re
from textgenrnn import textgenrnn


def process_tweet_text(text):
    text = re.sub(r'http\S+', '', text)   # Remove URLs
    text = re.sub(r'@[a-zA-Z0-9_]+', '', text)  # Remove @ mentions
    text = text.strip(" ")   # Remove whitespace resulting from above
    text = re.sub(r' +', ' ', text)   # Remove redundant spaces

    # Handle common HTML entities
    text = re.sub(r'&lt;', '<', text)
    text = re.sub(r'&gt;', '>', text)
    text = re.sub(r'&amp;', '&', text)
    return text


with open("config.yml", "r") as f:
    cfg = yaml.load(f)

auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
auth.set_access_token(cfg['access_key'], cfg['access_secret'])

api = tweepy.API(auth)

texts = []
context_labels = []

for user in cfg['twitter_users']:
    print("Downloading {}'s Tweets...".format(user))
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

textgen = textgenrnn(name='{}_twitter'.format("_".join(cfg['twitter_users'])))

if cfg['new_model']:
    textgen.train_new_model(
        texts,
        context_labels=context_labels,
        num_epochs=cfg['num_epochs'],
        gen_epochs=cfg['gen_epochs'],
        batch_size=cfg['batch_size'],
        prop_keep=cfg['prop_keep'],
        rnn_layers=cfg['model_config']['rnn_layers'],
        rnn_size=cfg['model_config']['rnn_size'],
        rnn_bidirectional=cfg['model_config']['rnn_bidirectional'],
        max_length=cfg['model_config']['max_length'],
        dim_embeddings=cfg['model_config']['dim_embeddings'],
        word_level=cfg['model_config']['word_level'])
else:
    textgen.train_on_texts(
        texts,
        context_labels=context_labels,
        num_epochs=cfg['num_epochs'],
        gen_epochs=cfg['gen_epochs'],
        prop_keep=cfg['prop_keep'],
        batch_size=cfg['batch_size'])
