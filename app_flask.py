from flask import Flask, render_template, request, redirect, jsonify
from pymongo import MongoClient

app = Flask(__name__)

# Liste des utilisateurs (données fictives pour cet exemple)
users = [
    {'id': 1, 'name': 'Alice', 'email': 'alice@example.com'},
    {'id': 2, 'name': 'Bob', 'email': 'bob@example.com'},
    {'id': 3, 'name': 'Charlie', 'email': 'charlie@example.com'}
]

@app.route('/')
def home():
    return "bonjour"


if __name__ == '__main__':
    app.run(debug=True)




app = Flask(__name__)
client = MongoClient('mongodb://localhost:27017/')
db = client['user_database']

@app.route('/users', methods=['GET'])
def get_users():
    users = db.users.find()
    user_list = []
    for user in users:
        user_list.append({'username': user['username'], 'email': user['email']})
    return jsonify({'users': user_list})

@app.route('/users', methods=['POST'])
def create_user():
    user_data = request.get_json()
    db.users.insert_one(user_data)
    return jsonify({'message': 'User created successfully'})

if __name__ == '__main__':
    app.run(debug=True)

