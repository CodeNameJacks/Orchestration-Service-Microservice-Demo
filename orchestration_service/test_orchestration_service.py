import os
import unittest
from unittest.mock import patch
import requests
from flask import jsonify
import json
import random
#import orchestration_service 


class testOrchestrate():
    
    def getUser(url, timeout=1): #use this to test getSubscription getPreference
        return requests.get(url).json()
    
    def testUrl(url): 
        try:
            r=requests.get(url, timeout=1)
            r.raise_for_status()
            return r.status_code
        except requests.exceptions.Timeout as errt:
            print (errt)
            raise
        except requests.exceptions.HTTPError as errh:
            print (errh)
            raise
        except requests.exceptions.ConnectionError as errc:
            print (errc)
            raise
        except requests.exceptions.RequestException as err:
            print (err)
            raise
       
        
        

class Testorchestration_service(unittest.TestCase):
    
    #def __init__(self, orchestration_service):
       #self.orchestration_service = orchestration_service

    id = random.randint(1, 1000)

    #test user sevices
    def test_valid_userUrl(self):
        #id = str(random.randint(1, 1000))
        self.assertEqual(200,testOrchestrate.testUrl('http://localhost:5000/user/' + str(random.randint(1, 1000))))

    def test_userException(self):
        self.assertRaises(requests.exceptions.HTTPError,testOrchestrate.testUrl,'http://localhost:5000/1001')

    def test_userResults(self):
        user_profile = testOrchestrate.getUser("http://localhost:5000/user/123")
        #user_data = user_profile.json()
        self.assertEqual(user_profile[0]["first_name"], "Billye")
    
    #test subscription services
    def test_valid_subscriptionUrl(self):
        self.assertEqual(200,testOrchestrate.testUrl('http://localhost:5002/subscription/user/'+ str(random.randint(1, 1000))))

    def test_subscriptionException(self):
        self.assertRaises(requests.exceptions.HTTPError,testOrchestrate.testUrl,'http://localhost:5002/subscription/user/1001')

    def test_subscriptionResults(self):
        user_subscription = testOrchestrate.getUser("http://localhost:5002/subscription/user/123")
        #user_data = user_profile.json()
        self.assertEqual(user_subscription[0]["status"], "Active")
    
    #test preference services    
    def test_valid_preferenceUrl(self):
        self.assertEqual(200,testOrchestrate.testUrl('http://localhost:5004/preferences/user/'+ str(random.randint(1, 1000))))

    def test_preferenceException(self):
        self.assertRaises(requests.exceptions.HTTPError,testOrchestrate.testUrl,'http://localhost:5004/preferences/user/1001')

    # def test_preferenceResults(self):
    #    user_preference = testOrchestrate.getUser("http://localhost:5004/preferences/user/21")
    #    self.assertIn(user_preference['Curio']['can_email'], ["true","false"])      


    #test orchestration service
    def test_valid_userSubscription(self):
        self.assertEqual(200,testOrchestrate.testUrl('http://localhost:5006/user/details/' + str(random.randint(1, 1000))))

    def test_valid_userDetails(self):
        self.assertEqual(200,testOrchestrate.testUrl('http://localhost:5006/user/subscription/' + str(random.randint(1, 1000))))

    
if __name__ == '__main__':
    unittest.main()
