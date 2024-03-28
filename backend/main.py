import os
from flask import Flask, request, jsonify
from pymongo import MongoClient
from flask_cors import CORS 
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Read environment variable
mongo_uri = os.getenv('MONGO_URI')


app = Flask(__name__)

CORS(app)

client = MongoClient(mongo_uri)
db = client.get_database("Docker_User")

# Use the appropriate collection name
collection = db['users']

@app.route('/store-data', methods=['POST'])
def store_data():
    name = request.form['name']
    email = request.form['email']
    collection.insert_one({'name': name, 'email': email})
    return jsonify({'message': 'Data stored successfully!'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
