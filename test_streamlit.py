import streamlit as st
from pymongo import MongoClient
import os

# Informations de connexion à MongoDB
user = os.environ.get("MONGO_USER")
password = os.environ.get("MONGO_PASSWORD")
host = os.environ.get("MONGO_HOST")
dbname = os.environ.get("MONGO_DBNAME")
collection_name = os.environ.get("MONGO_COLLECTION_NAME")
app_name = os.environ.get("MONGO_APP_NAME")

# Construction de l'URI de connexion à MongoDB
uri = f"mongodb+srv://{user}:{password}@{host}/{dbname}?retryWrites=true&w=majority&appName={app_name}&tls=true"

print(uri)
# Connexion à MongoDB
client = MongoClient(uri)
db = client[dbname]
collection = db[collection_name]

# Récupération des données
cursor = collection.find({})
data = list(cursor)

# Affichage des données dans Streamlit
st.write(data)
