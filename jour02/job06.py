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
# Requête SQL pour calculer la superficie totale des étages
query = "SELECT SUM(capacite) AS capacite_totale FROM salle"

# Exécution de la requête
cursor.execute(query)

# Récupération du résultat
resultat = cursor.fetchone()
capacite_totale = resultat[0]

# Affichage du résultat
print(f"La capacité des salles est de : {capacite_totale} ")

# Fermeture du curseur et de la connexion
cursor.close()
connection.close()