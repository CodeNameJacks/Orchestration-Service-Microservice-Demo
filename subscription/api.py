from flask import Flask
from flask import jsonify

app = Flask(__name__)

# use to test initial set up of flask server
@app.route('/api/test')
def testAppConnect():
    return {'response': "Subscription service is working and backend is running"}
