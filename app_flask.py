#import librairies 
from flask import Flask, request, jsonify
from pymongo import MongoClient


app = Flask(__name__)

#Connexion à MongoDb
client = MongoClient('mongodb://mongo:27017')  

@app.route('/users', methods=['GET'])
def get_users():
    # Récupèrer les utilisateurs de la base de données et les renvoyer sous forme de JSON
    users = client.db.users.find()
    return jsonify([{'name': user['name'], 'email': user['email']} for user in users])

# Liste des utilisateurs de base (données fictives pour cet exemple)
users = [
    {'id': 1, 'name': 'Lucas', 'email': 'Lucas@example.com'},
    {'id': 2, 'name': 'Lahcene', 'email': 'Lahcene@example.com'},
    {'id': 3, 'name': 'Charlotte', 'email': 'charlotte@example.com'}
    ]



# opérations de création, de mise à jour et de suppression (CRUD)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

