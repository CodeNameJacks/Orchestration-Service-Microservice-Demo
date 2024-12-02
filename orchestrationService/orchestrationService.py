import os
from flask import Flask
from flask import jsonify
from dotenv import load_dotenv, dotenv_values 
import mysql.connector
import json
import requests
from array import array
from collections import OrderedDict

app = Flask(__name__)

# loading variables from .env file
load_dotenv() 

    
class OrchestrateService:
    
    
    #define and set environment variable urls for the microservices
    global USER_SERV_URL 
    global SUB_SERV_URL 
    global PREF_SERV_URL 
    
    USER_SERV_URL =  os.getenv('URL_USER_SERV')
    SUB_SERV_URL = os.getenv('URL_SUB_SERV')
    PREF_SERV_URL = os.getenv('URL_PREF_SERV')
    
    
    
    #### --- HELPER FUNCTION  ------#####
    
    # function that makes url call to get user info
    # @params id (user id)
    def get_userInfo(id):
        response = requests.get(f"{USER_SERV_URL}/user/{id}")
        if(response.status_code != 200):
            raise Exception ("User {id} does not exits. Please try a different user id") 
        else: 
            return response.json()
        
        
    # function that makes url call to get user subscription info
    # @params id (user id)
    def get_userSubInfo(id): 
        response = requests.get(f"{SUB_SERV_URL}/subscription/user/{id}") 
        if(response.status_code != 200):
            return ("Obtaining user subscription information failed for user id {id}. Please try again") 
        else: 
            return response.json()  
        
    # function that makes url call to get user preference info
    # @params id (user id) 
    def get_userPrefInfo(id): 
        response = requests.get(f"{PREF_SERV_URL}/preferences/user/{id}")  
        if(response.status_code != 200):
            return ("There are no preferneces set for user id {id}") 
        else: 
            return response.json()  
               
    
        
    #### --- APIs ------#####       
    
    # use to test initial set up of flask server
    @app.route('/api/test')
    def testAppConnect():
        return {'response': "Orchestrate service is working and backend is running"}

         
    # Retrieves user information along with active subscription information
    # @params id (user_id)
    @app.route('/user/subscription/<id>', methods = ['GET'])    
    def subscription(id):
        
        user_data = OrchestrateService.get_userInfo(id)
        sub_data = OrchestrateService.get_userSubInfo(id)
        
        results = { "USER INFO" : user_data[0],
                   "SUBSCRIPTION INFO" : sub_data
                  }
          
        return str(results)
    
    
    #Retrieves user dettails, subscription status and prefernce by product. 
    # @params id (user_id)
    @app.route('/user/details/<id>', methods = ['GET']) 
    def details(id):
        user_data = OrchestrateService.get_userInfo(id)
        sub_data = OrchestrateService.get_userSubInfo(id)
        pref_data = OrchestrateService.get_userPrefInfo(id)
        
        results = { "USER INFO" : user_data[0],
                   "SUBSCRIPTION INFO" : sub_data[0]['status'],
                   "PREFERENCES INFO" : pref_data
                  }
          
        return str(results)
    
    if __name__ == '__main__':
        app.run(port=5006)

