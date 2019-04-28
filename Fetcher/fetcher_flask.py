'''
Created on Dec 04, 2018

@author: Gabriel Torrandella
'''
from flask import Flask, json, jsonify
from flask.globals import request
from flask.wrappers import Response

from Fetcher.fetcher import Fetcher
from Campaign.Campaign import Campaign

def fixDate(stringDate):
    dateList = []
    for d in stringDate.split('-'):
        for ds in d.split(' '):
            dateList.append(ds)
    date = dateList[0] + " " + dateList[1] + " " + dateList[2] + " " + dateList[3]
    return date

app = Flask(__name__)

fetcher = Fetcher()

def check(json):
    k = json.keys()
    return ('id' in k and 'email' in k and "hashtags" in k and "mentions" in k and "startDate" in k and "finDate" in k) 

@app.route('/fetcher', methods = ['GET', 'POST'])
def api_fetcher():
    if 'Content-Type' in request.headers.keys():
        if request.headers['Content-Type'] == 'application/json':
            cJson = json.loads(request.json)
            if check(cJson):
                campaign = Campaign(cJson["id"],cJson["email"],cJson["hashtags"],cJson["mentions"],cJson["startDate"],cJson["finDate"])
                                        
                fetcher.fetchTweets(campaign)

                return Response(status = 200)
            else:
                return Response(status = 400)
        else:
            return Response(400)
                
    else:
        return Response(status = 400)


if __name__ == "__main__":
    app.run(host='0.0.0.0')
