import mysql.connector

class zoo:
    def __init__(self, host, user, password, database):
        self.connexion = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.curseur = self.connexion.cursor()

    def ajouter_animal(self, nom, race, cage_id, date_naissance, pays_origine):
        requete = "INSERT INTO animal (nom, race, id_cage, date_naissance, pays_origine) VALUES (%s, %s, %s, %s, %s)"
        valeurs = (nom, race, cage_id, date_naissance, pays_origine)
        self.curseur.execute(requete, valeurs)
        self.connexion.commit()

    def supprimer_animal(self, id_animal):
        requete = "DELETE FROM animal WHERE id = %s"
        self.curseur.execute(requete, (id_animal,))
        self.connexion.commit()

    def modifier_animal(self, id_animal, nom, race, cage_id, date_naissance, pays_origine):
        requete = "UPDATE animal SET nom=%s, race=%s, id_cage=%s, date_naissance=%s, pays_origine=%s WHERE id=%s"
        valeurs = (nom, race, cage_id, date_naissance, pays_origine, id_animal)
        self.curseur.execute(requete, valeurs)
        self.connexion.commit()

    def afficher_animaux(self):
        requete = "SELECT * FROM animal"
        self.curseur.execute(requete)
        animaux = self.curseur.fetchall()
        return animaux

    def afficher_animaux_cages(self):
        requete = """
            SELECT a.*, c.superficie, c.capacite_max
            FROM animal a
            LEFT JOIN cage c ON a.cage_id = c.id
        """
        self.curseur.execute(requete)
        animaux_cages = self.curseur.fetchall()
        return animaux_cages

    def calculer_superficie_totale(self):
        requete = "SELECT SUM(superficie) FROM cage"
        self.curseur.execute(requete)
        superficie_totale = self.curseur.fetchone()[0]
        return superficie_totale

    def fermer_connexion(self):
        self.curseur.close()
        self.connexion.close()

# Exemple d'utilisation de la classe ZooManager
zoo = zoo("localhost", "amandine", "eminem06", "zoo")

# Ajout d'un animal
zoo.ajouter_animal("Lion", "Sauvage", 1, "2020-01-01", "Afrique")

# Affichage des animaux
animaux = zoo.afficher_animaux()
print("Animaux dans le zoo:")
for animal in animaux:
    print(animal)

# Affichage des animaux dans les cages
animaux_cages = zoo.afficher_animaux_cages()
print("\nAnimaux dans les cages avec superficie et capacité max:")
for animal in animaux_cages:
    print(animal)

# Calcul de la superficie totale des cages
superficie_totale = zoo.calculer_superficie_totale()
print(f"\nSuperficie totale des cages : {superficie_totale} m2")

# Fermeture de la connexion
zoo.fermer_connexion()
