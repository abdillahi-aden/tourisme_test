from pymongo import MongoClient
import json
import os

# Connexion à MongoDB
client = MongoClient(
    host="127.0.0.1",
    port=27017,
    username="admin",
    password="pass"
)

db = client["tourisme"]  # Nom de votre base de données
collection = db["test_v1"]  # Nom de votre collection

# Chemin vers le dossier principal extrait de votre fichier ZIP
objects_path = '/home/ubuntu/donnee_mongo/script/extrait/objects'  # Remplacez avec le chemin correct

# Fonction pour importer les fichiers JSON d'un sous-sous-dossier
def import_json_from_subfolder(subfolder_path):
    for file_name in os.listdir(subfolder_path):
        if file_name.endswith('.json'):
            with open(os.path.join(subfolder_path, file_name), 'r', encoding='utf-8') as file:
                data = json.load(file)
                collection.insert_one(data)

# Parcours de chaque sous-dossier dans chaque dossier principal et importation des fichiers JSON
for folder in os.listdir(objects_path):
    folder_path = os.path.join(objects_path, folder)
    if os.path.isdir(folder_path):
        for subfolder in os.listdir(folder_path):
            subfolder_path = os.path.join(folder_path, subfolder)
            if os.path.isdir(subfolder_path):
                import_json_from_subfolder(subfolder_path)

print("Données importées avec succès dans MongoDB.")
