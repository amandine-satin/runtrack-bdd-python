import mysql.connector
# Remplacez les valeurs suivantes par les informations de votre base de données
host = "localhost"
user = "amandine"
password = "eminem06"
database = "LaPlateforme"

# Connexion à la base de données
connection = mysql.connector.connect(
    host=host,
    user=user,
    password=password,
    database=database
)

 # Création d'un curseur
cursor = connection.cursor()

# # Exécution de la requête pour récupérer tous les étudiants
query = "SELECT * FROM etudiants"
cursor.execute(query)

# # Récupération des résultats
etudiants = cursor.fetchall()

 # Affichage des résultats
for etudiant in etudiants:
 print(etudiant)

# # Fermeture du curseur et de la connexion
cursor.close()
connection.close()
 