"""Script de l'étape 2 : affiche des informations sur l'environnement d'exécution,
puis calcule un chiffre d'affaires avec pandas."""
import platform
import socket

import pandas as pd

ventes = pd.DataFrame({
    "produit": ["clavier", "souris", "ecran", "casque"],
    "prix": [49.90, 19.90, 189.00, 79.00],
    "quantite": [3, 5, 2, 4],
})
ventes["total"] = ventes["prix"] * ventes["quantite"]

print("Bonjour depuis un conteneur Docker !")
print(f"Nom de la machine : {socket.gethostname()}")
print(f"Python {platform.python_version()} | pandas {pd.__version__}")
print(f"Chiffre d'affaires total : {ventes['total'].sum():.2f} EUR")
