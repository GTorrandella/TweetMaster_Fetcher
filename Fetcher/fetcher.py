'''
Created on Nov 20, 2018

@author: Gabriel Torrandella
'''
from os import path

from twython import Twython

from Tweet.Tweet import Tweet


parentDir = path.dirname(path.abspath(__file__))
tokenPath = path.join(parentDir, 'tokens')
f = open(tokenPath)
APP_KEY = f.readline()
APP_SECRET = f.readline()
ACCESS_TOKEN = f.readline().rstrip()
f.close

class Fetcher():
    twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
    twitter = Twython(APP_KEY, access_token=ACCESS_TOKEN)
    
    def fetchByHashtag(self, hashtag):
        rawTweet = self.twitter.cursor(self.twitter.search, q=hashtag, result_type="recent")
        return rawTweet
    
    def fetchByMention(self, mention):
        rawTweet = self.twitter.cursor(self.twitter.search, q=mention, result_type="recent")
        return rawTweet
    
    def makeTweet(self, rawTweets):
        tweets = []
        for tweetContent in rawTweets:
            for tweet in tweetContent:
                tweets.append(Tweet(tweet).to_json())
        return {'Tweets':tweets}
            
    def fetchTweets(self, campaign):
        rawTweets = []
        
        for hashtag in campaign.hashtags:
            rawTweets.append(self.fetchByHashtag(hashtag))
            
        for mention in campaign.mentions:
            rawTweets.append(self.fetchByMention(mention))
               
        return self.makeTweet(rawTweets)