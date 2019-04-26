'''
Created on Nov 20, 2018

@author: Gabriel Torrandella
'''
import unittest

from Campaign.Campaign import Campaign
from Tweet.Tweet import Tweet


class test_fetcher_base(unittest.TestCase):
    
    def setUp(self):
        self.lastId = "967824267948770000"

        self.campaign = Campaign("idC", "emailDueño", ["#mars"], ["@mars"], "06 12 2018 23:20:00", "07 12 2018 00:00:30")

        self.hastag = {
                "statuses": [
                        {
                                "created_at": "Sun Feb 25 18:11:01 +0000 2018",
                                "id_str": "967824267948773377",
                                "entities": {
                                        "hashtags": ["mars"],
                                        "symbols": [],
                                        "user_mentions": [],
                                        },
                                "user": {
                                        "id_str": "11348282",
                                        "name": "NASA"
                                        }
                        },
                        {
                                "created_at": "Sun Feb 25 18:11:01 +0000 2018",
                                "id_str": "967824267948773378",
                                "entities": {
                                        "hashtags": ["mars"],
                                        "symbols": [],
                                        "user_mentions": [],
                                        },
                                "user": {
                                        "id_str": "11348282",
                                        "name": "NASA"
                                        }
                        }
                    ]
        }
        
        self.mention = {
                "statuses": [
                        {
                                "created_at": "Sun Feb 25 18:11:01 +0000 2018",
                                "id_str": "967824267948773377",
                                "entities": {
                                        "hashtags": [],
                                        "user_mentions": ["mars"],
                                        },
                                "user": {
                                        "id_str": "11348282",
                                        "name": "NASA"
                                        }
                        },
                        {
                                "created_at": "Sun Feb 25 18:11:01 +0000 2018",
                                "id_str": "967824267948773378",
                                "entities": {
                                        "hashtags": [],
                                        "user_mentions": ["mars"],
                                        },
                                "user": {
                                        "id_str": "11348282",
                                        "name": "NASA"
                                        }
                        }
                    ]
        }
        
        self.responseHastag = [self.hastag["statuses"][0], self.hastag["statuses"][1]]
        self.responseMention = [self.mention["statuses"][0], self.mention["statuses"][1]]
        
        self.param_makeTweets = self.responseHastag + self.responseMention
        
        self.response_fetchTweets = {'Tweets':[Tweet(self.responseHastag[0]).to_json(),Tweet(self.responseHastag[1]).to_json(),Tweet(self.responseMention[0]).to_json(),Tweet(self.responseMention[1]).to_json()]}
        
        self.resquest_get_200_content = self.campaign.to_json()
    
            