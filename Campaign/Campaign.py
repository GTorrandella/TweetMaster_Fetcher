from datetime import datetime
from _datetime import datetime
import json

class Campaign(object):

    def __init__(self, idC, emailDueño, hashtags, mentions, startDate, finDate):
        '''  Constructor '''
        self.idC=idC
        self.emailDueño = emailDueño
        self.hashtags = hashtags  
        self.mentions = mentions  
        self.startDate = datetime.strptime(startDate, "%d %m %Y %X") #dd mm yyyy hh:mm:ss
        self.finDate = datetime.strptime(finDate, "%d %m %Y %X") #dd mm yyyy hh:mm:ss

    def to_json(self):
        dictionary = self.to_dict() #Llamamos a la funcion de abajo
        camp_json = json.dumps(dictionary) 
        return camp_json

    def to_dict(self):
        dictionary = {
            'id' : self.idC,
            'email' : self.emailDueño,
            'hashtags' : self.hashtags,
            'mentions' : self.mentions,
            'startDate' : datetime.strftime(self.startDate,"%d %m %Y %X"),
            'finDate' : datetime.strftime(self.finDate,"%d %m %Y %X"),
        }
        return dictionary

    def isActive(self): #OK
        if ((datetime.now() > self.startDate) and (datetime.now() < self.finDate)):
            return True
        return False

    def isFinished(self):   #OK
        if (datetime.now() > self.finDate):
            return True
        return False
    
    def __repr__(self):
        return "<idC:%s emailDueño:%s hashtags:%s mentions:%s startDate:%s finDate:%s> " % (self.idC, self.emailDueño, self.hashtags, self.mentions, self.startDate, self.finDate)
    
        
    