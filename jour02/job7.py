import mysql.connector

class Employe:
    def __init__(self, host, user, password, database):
        self.connexion = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.curseur = self.connexion.cursor()

    def ajouter_employe(self, nom, prenom, salaire, id_service):
        requete = "INSERT INTO employe (nom, prenom, salaire, id_service) VALUES (%s, %s, %s, %s)"
        valeurs = (nom, prenom, salaire, id_service)
        self.curseur.execute(requete, valeurs)
        self.connexion.commit()

    def recuperer_employes_salaire_superieur_a(self, seuil_salaire):
        requete = "SELECT * FROM employe WHERE salaire > %s"
        self.curseur.execute(requete, (seuil_salaire,))
        employes = self.curseur.fetchall()
        return employes

    def recuperer_employes_et_service(self):
        requete = """
            SELECT e.*, s.nom AS service_nom
            FROM employe e
            JOIN service s ON e.id_service = s.id
        """
        self.curseur.execute(requete)
        employes_service = self.curseur.fetchall()
        return employes_service

    def fermer_connexion(self):
        self.curseur.close()
        self.connexion.close()

# Utilisation de la classe EmployeManager
employe_manager = Employe("localhost", "amandine", "eminem06", "Gestions")

# Ajout d'un employé
employe_manager.ajouter_employe("NouveauNom", "NouveauPrenom", 3200.00, 2)

# Récupération des employés dont le salaire est supérieur à 3000 €
employes_salaire_superieur = employe_manager.recuperer_employes_salaire_superieur_a(3000.00)
print("Employés dont le salaire est supérieur à 3000 €:")
for employe in employes_salaire_superieur:
    print(employe)

# Récupération de tous les employés et leur service respectif
employes_service = employe_manager.recuperer_employes_et_service()
print("\nEmployés et leur service respectif:")
for employe in employes_service:
    print(employe)

# Fermeture de la connexion
employe_manager.fermer_connexion()

