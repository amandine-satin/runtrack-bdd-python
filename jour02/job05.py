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
query = "SELECT SUM(superficie) AS superficie_totale FROM etage"

# Exécution de la requête
cursor.execute(query)

# Récupération du résultat
resultat = cursor.fetchone()
superficie_totale = resultat[0]

# Affichage du résultat
print(f"La superficie de La Plateforme est de {superficie_totale} m2")

# Fermeture du curseur et de la connexion
cursor.close()
connection.close()