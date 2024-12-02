import os
from flask import Flask
from flask import jsonify
from dotenv import load_dotenv, dotenv_values 
import mysql.connector
import json
from array import array

app = Flask(__name__)

# loading variables from .env file
load_dotenv() 

class Preference:
    # use to test initial set up of flask server
    @app.route('/api/test')
    def testAppConnect():
        return {'response': "User service is working and backend is running"}


    # preference service api that returns user preferences info
    # @params id (user_id)
    @app.route('/preferences/user/<id>', methods = ['GET', 'PUT'])
    def user(id):
        try:
            #establish database connection
            mydb = mysql.connector.connect(
                host = os.getenv('DB_HOST'),
                user = os.getenv('DB_USER'),
                port = os.getenv('DB_PORT'),
                password = os.getenv('DB_PWD'),
                database = os.getenv('DB_USER_SERV')
            )
            
            cursor = mydb.cursor()
            sqltext = 'SELECT product, chosen_mode as mode, local as location, notifications as notify_enabled, email_permission as can_email, is_subscribed_to_newsletter from preference.preference where id ='
            cursor.execute(sqltext + id)
            row_headers=[x[0] for x in cursor.description]
            res = cursor.fetchall()
            json_data=[]
            #items = len(res[0])
            for x in res:
                    json_data.append(x[0]+":"
                        "mode"+":"+ x[1]+' '+
                        "location"+":"+ x[2]+' '+
                        "notify_enabled"+":"+ x[3]+' '+
                        "can_email"+":"+ x[4]+' '+
                        "is_subscribed_to_newsletter"+":"+ x[5])
                    
                
            #close database connection   
            cursor.close()
            mydb.close() 
            
            if(json_data):
                return json.dumps(json_data)
            else:
                return("No preference have been set for this user")
        except:
            print("Someting went wrong getting user preferences")

    if __name__ == '__main__':
        app.run(port=5004)

