import json

class Tweet(object):
    '''classdocs'''
    def __init__(self, tweet):
        ''' Constructor '''
        self.ID = tweet['id_str']
        user = tweet['user'];
        entities = tweet['entities'] #diccionario con 2 listas (hashtags y mentions)
        self.userName = user['name']
        self.userID = user['id_str']
        
        self.hashtags = []
        if type(entities['hashtags']) == dict:
            self.hashtags.append('#'+entities['hashtags']['text'])
        else:
            for d in entities['hashtags']:
                if type(d) == dict:
                    self.hashtags.append('#'+d['text'])
                else:
                    self.hashtags.append(d)
        
        self.mentions = []
        if type(entities['user_mentions']) == dict:
            self.mentions.append('@'+entities['user_mentions']['screen_name'])
        else:
            if type(entities['user_mentions']) == list:
                for d in entities['user_mentions']:
                    if type(d) == dict:
                        self.mentions.append('@'+d['screen_name'])
                    else:
                        self.mentions.append(d)
                        
        self.date = tweet['created_at']
        #Sun Mar 20 21:08:01 2018"


    def to_json(self):
        dictionary = {
            "id_str" : self.ID,
            "user" : {"name" : self.userName, "id_str" : self.userID},
            "entities" : {"hashtags" : self.hashtags,
            "user_mentions" : self.mentions},
            "created_at" : str(self.date)
        }
        tweet_json = json.dumps(dictionary) 
        return tweet_json
