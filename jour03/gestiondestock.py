import tkinter as tk
import tkinter.ttk as ttk
import mysql.connector

# Fonction pour ajouter un produit
def ajouter_produit():
    nom = entry_nom.get()
    description = entry_description.get("1.0", tk.END)
    price = entry_price.get()
    entry_quantity = entry_quantity.get()
    category_id = entry_category.get()

    cursor.execute("INSERT INTO product (name, description, price, quantity, id_category) VALUES (%s, %s, %s, %s, %s)",
                   (nom, description, price, quantity, categorie_id))
    conn.commit()
    afficher_produits()
0
# Fonction pour supprimer un produit
def supprimer_produit():
    produit_id = entry_id.get()
    cursor.execute("DELETE FROM product WHERE id=%s", (produit_id,))
    conn.commit()
    afficher_produits()

# Fonction pour modifier un produit
def modifier_produit():
    produit_id = entry_id.get()
    quantity = entry_quantity.get()
    price = entry_price.get()

    cursor.execute("UPDATE product SET quantity=%s, price=%s WHERE id=%s", (quantity, price, produit_id))
    conn.commit()
    afficher_produits()

# Fonction pour afficher les produits
def afficher_produits():
    cursor.execute("SELECT * FROM product")
    product = cursor.fetchall()

    # Effacer les lignes précédentes
    for i in treeview.get_children():
        treeview.delete(i)

    # Afficher les produits dans le tableau
    for product in product:
        treeview.insert("", "end", values=product)

# Connexion à la base de données MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="amandine",
    password="eminem06",
    database="store"
)
cursor = conn.cursor()

# Création de l'interface graphique
root = tk.Tk()
root.title("Gestion des stocks")

# Entrées pour ajouter un produit
tk.Label(root, text="Nom du produit:").grid(row=0, column=0)
entry_nom = tk.Entry(root)
entry_nom.grid(row=0, column=1)

tk.Label(root, text="Description du produit:").grid(row=1, column=0)
entry_description = tk.Text(root, height=4, width=30)
entry_description.grid(row=1, column=1)

tk.Label(root, text="Prix du produit:").grid(row=2, column=0)
entry_price = tk.Entry(root)
entry_price.grid(row=2, column=1)

tk.Label(root, text="Quantité du produit:").grid(row=3, column=0)
entry_quantity = tk.Entry(root)
entry_quantity.grid(row=3, column=1)

tk.Label(root, text="ID de catégorie:").grid(row=4, column=0)
entry_category = tk.Entry(root)
entry_category.grid(row=4, column=1)

# Boutons pour ajouter, supprimer et modifier un produit
btn_ajouter = tk.Button(root, text="Ajouter produit", command=ajouter_produit)
btn_ajouter.grid(row=5, column=0)

tk.Label(root, text="ID du produit à supprimer/modifier:").grid(row=6, column=0)
entry_id = tk.Entry(root)
entry_id.grid(row=6, column=1)

btn_supprimer = tk.Button(root, text="Supprimer produit", command=supprimer_produit)
btn_supprimer.grid(row=7, column=0)

btn_modifier = tk.Button(root, text="Modifier produit", command=modifier_produit)
btn_modifier.grid(row=7, column=1)

# Tableau pour afficher les produits
treeview = ttk.Treeview(root, columns=("ID", "Nom", "Description", "Price", "Quantity", "ID catégorie"))
treeview.grid(row=8, column=0, columnspan=2)
treeview.heading("#0", text="ID")
treeview.column("#0", minwidth=0, width=50, stretch=tk.NO)
treeview.heading("#1", text="Nom")
treeview.heading("#2", text="Description")
treeview.heading("#3", text="Price")
treeview.heading("#4", text="Quantity")
treeview.heading("#5", text="ID catégorie")

# Afficher les produits
afficher_produits()

root.mainloop()