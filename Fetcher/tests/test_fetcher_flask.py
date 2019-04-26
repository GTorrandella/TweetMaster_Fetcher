'''
Created on Nov 20, 2018

@author: Gabriel Torrandella
'''
import unittest
from unittest.mock import MagicMock

from Fetcher.fetcher import Fetcher
import Fetcher.fetcher_flask as fetcher_flask
from Fetcher.tests.test_fetcher_base import test_fetcher_base


class test_fetcher_flask(test_fetcher_base):

    def return_values(self, search, q, result_type):
        if q == "#mars":
            return self.responseHastag
        
        if q == "@mars":
            return self.responseMention

        
    def setUp(self):
        test_fetcher_base.setUp(self)
        
        self.test_app = fetcher_flask.app.test_client()
        self.ctx = fetcher_flask.app.app_context()
        self.ctx.push()
        
        Fetcher().twitter.cursor = MagicMock(side_effect = self.return_values)

    def tearDown(self):
        self.ctx.pop()


    def test_GET_200(self):
        response = self.test_app.get('/fetcher',json=self.resquest_get_200_content, content_type = 'application/json')
        
        self.assertEqual(response.status, '200 OK')
        self.assertTrue('Content-Type' in response.headers.keys())
        self.assertEqual('application/json', response.headers['Content-Type'])
        self.assertEqual(self.response_fetchTweets, response.json)
        
    def test_GET_400(self):
        response = self.test_app.get('/fetcher', content_type = 'application/json')
        
        self.assertEqual(response.status, '400 BAD REQUEST')

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test_correctPut']
    unittest.main()