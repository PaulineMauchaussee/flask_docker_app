#import librairies 
from flask import Flask, request, jsonify
from pymongo import MongoClient
import os

#Création de mon application
app = Flask(__name__)
port=27017

#information de connexion à la base de données
host = os.environ.get('MONGO_HOST', "localhost")

#création du client de connexion
client= MongoClient(host=host, port=port)

mabdd= client.demo
@app.route('/')
def hello_world():
   return "Hello World! \n" + str(type(mabdd)) + '\n mabdd : \n' + str(mabdd)


#test flask 
@app.route("/poulet/ <msg>", methods=["GET"])
def poulet(msg):
        return f'boujour{msg}'

#method find by id 
@app.route("/users", methods=["GET"])
def get_users():
     return "tous les users"

#method read all
@app.route("/users/<id>", methods=["GET"])
def get_user():
     return f'Le user qui a l\'id :{id}'

#method pour créer un user 
@app.route("/users", methods=["POST"])
def create_user():
     return None

#method pour mettre à jour 
@app.route("/users/<id>", methods=["PUT"])
def update_user(id):
     return None

#method pour supprimer
@app.route("/users/<id>", methods=["DELETE"])
def delete_user(id):
     return None


# Lancement de mon application

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9001)


#Get = récuperer les sinfos 
#Post = envoyer des infos
#Put =  reçoit des infos et les met à jour
#Delete = supprimer des infos