""""
exemple de communication avec une base de mongodb 
Lexique: 
* Base de données <=> database
* table <=> collection

"""
#import de mes librairies 
from pymongo import MongoClient
# info de ma base de données 
host = "localhost"
port = 27017

#création du client de connexion 
client = MongoClient(host=host, port=port)

#récupération de ma base de données 
mabdd = client.demo

print("ma bdd : \n", type(mabdd))
print("mabdd : \n", mabdd)