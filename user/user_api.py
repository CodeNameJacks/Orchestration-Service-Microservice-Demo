import os
from flask import Flask
from flask import jsonify
from dotenv import load_dotenv, dotenv_values 
import mysql.connector
import json

app = Flask(__name__)

# loading variables from .env file
load_dotenv() 

class User:
    # use to test initial set up of flask server
    @app.route('/api/test')
    def testAppConnect():
        return {'response': "User service is working and backend is running"}

    # API to retrieve user info from database
    # @params id (user_id)
    @app.route('/user/<id>', methods = ['GET', 'PUT'])
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
            sqltext = 'SELECT id as user_id, first as first_name, last as last_name, postal as postal_code, dob as birth_date, email from user.user where id ='
            cursor.execute(sqltext + id)
            row_headers=[x[0] for x in cursor.description]
            res = cursor.fetchall()
            json_data=[]
            for result in res:
                json_data.append(dict(zip(row_headers,result)))
            
            #close database connection   
            cursor.close()
            mydb.close() 
        
            if(json_data):
                return json.dumps(json_data)
            else:
                return response.status_code
        except:
            print("Someting went wrong in getting the User")


    if __name__ == '__main__':
        app.run(port=5000)

