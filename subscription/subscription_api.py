import os
from flask import Flask
from flask import jsonify
from dotenv import load_dotenv, dotenv_values 
import mysql.connector
import json

app = Flask(__name__)

# loading variables from .env file
load_dotenv() 

class Subscription:
    # use to test initial set up of flask server
    @app.route('/api/test')
    def testAppConnect():
        return {'response': "Subscription service is working and backend is running"}


    #subscription service api that returns user's subscription info from database
    # @params id (user_id)
    @app.route('/subscription/user/<id>', methods = ['GET', 'PUT'])
    def user(id):
        try:
            #establich database connection
            mydb = mysql.connector.connect(
                host = os.getenv('DB_HOST'),
                user = os.getenv('DB_USER'),
                port = os.getenv('DB_PORT'),
                password = os.getenv('DB_PWD'),
                database = os.getenv('DB_USER_SERV')
            )
            
            cursor = mydb.cursor()
            sqltext = 'SELECT accountFreq as accountType, dateRenew as renewalDate, dateRegistered as registrationDate, product, status, paymentType as paymentMethod from subscription.subscription where usr_id ='
            cursor.execute(sqltext + id)
            row_headers=[x[0] for x in cursor.description]
            res = cursor.fetchall()
            json_data=[]
            for result in res:
                json_data.append(dict(zip(row_headers,result)))
            
            #close database connections   
            cursor.close()
            mydb.close()
            
            if(json_data):    
                return json.dumps(json_data)
            else:
                return response.status_code
        except:
            print("Somthing went wrong pulling subscription info for user")

    if __name__ == '__main__':
        app.run(port=5002)

