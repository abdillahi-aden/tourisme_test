import pandas as pd
from pymongo import MongoClient


# Connexion à MongoDB
client = MongoClient(
    host="127.0.0.1",
    port=27017,
    username="admin",
    password="pass"
)

db = client["voyage_csv"]  # Nom de votre base de données
collection = db["test_v1"]  # Nom de votre collection

# Fonction pour lire un fichier CSV et le convertir en dictionnaire
def read_csv_to_dict(file_path):
    return pd.read_csv(file_path).to_dict('records')


# Chemins des fichiers CSV
chemin_datatourisme = '/home/ubuntu/donnee_mongo/datatourisme-tour-20231215.csv'
chemin_rhone_communes = '/home/ubuntu/donnee_mongo/rhone_communes_geo1.csv'

# Lecture et importation des données datatourisme
donnees_datatour = read_csv_to_dict(chemin_datatourisme)
poi_csv_test1 = db['poi_csv_test1']  # Remplacer par le nom de votre collection pour datatourisme
poi_csv_test1.insert_many(donnees_datatour)

# Lecture et importation des données rhone_communes
donnees_rhone_communes = read_csv_to_dict(chemin_rhone_communes)
commune_csv_test1 = db['commune_csv_test1']  # Remplacer par le nom de votre collection pour rhone_communes
commune_csv_test1.insert_many(donnees_rhone_communes)

print("Importation des données dans les collections distinctes terminée avec succès.")
