# Projet fil rouge Docker : point de départ

🇬🇧 *English version: branch [`main`](https://github.com/DataScientest/DS-Docker-Course-Architecture/tree/main).*

Ce dépôt est votre point de départ pour le cas pratique du module Docker. À la fin du module, il fera tourner trois conteneurs reliés par Docker Compose :

- **`db`** : une base de données MariaDB, qui contient 1 000 transactions clients ;
- **`train`** : un traitement ponctuel qui entraîne un modèle de détection de fraude à partir de ces transactions ;
- **`api`** : une API web FastAPI qui donne accès aux transactions et aux prédictions du modèle.

Tout le code (Python, SQL) est fourni : vous n'écrivez que la partie Docker. Suivez le cours étape par étape : il vous indique quand et comment compléter chaque fichier.

## Contenu du dépôt

```
DS-Docker-Course-Architecture/
├── etape2-premier-dockerfile/    l'exercice d'échauffement de l'étape 2 (hors projet)
│   ├── bonjour.py
│   ├── requirements.txt
│   └── Dockerfile                ✏️ modèle à trous (étape 2)
│
├── api/                          service api : l'API FastAPI
│   ├── main.py                   l'application (fournie)
│   ├── requirements.txt          ses dépendances (✏️ une ligne à ajouter à l'étape 8)
│   ├── Dockerfile                ✏️ à écrire (étape 4)
│   └── .dockerignore             ✏️ à compléter (étape 4)
├── db/                           service db : la base MariaDB
│   ├── Dockerfile                ✏️ à écrire (étape 5)
│   ├── init/
│   │   └── 01_transactions.sql   crée la table et y charge le CSV (fourni)
│   └── data/
│       └── transactions.csv      1 000 transactions clients fictives (fournies)
├── train/                        service train : l'entraînement du modèle
│   ├── train.py                  le script d'entraînement (fourni)
│   ├── requirements.txt          ses dépendances (fournies)
│   ├── Dockerfile                ✏️ à écrire (étape 8)
│   └── .dockerignore             ✏️ à compléter (étape 8)
└── compose.yaml                  ✏️ à écrire (étapes 6 et 8)
```

Chaque service a son dossier, qui porte son nom et contient son Dockerfile. Le dossier `etape2-premier-dockerfile/` ne fait pas partie du projet : c'est l'exercice de l'étape 2.

## Ce que vous allez compléter

Les fichiers marqués ✏️ ne contiennent pour l'instant que des commentaires, qui décrivent ce qu'ils doivent contenir.

| Fichier | Étape | Ce qu'il faut faire |
|---|---|---|
| `etape2-premier-dockerfile/Dockerfile` | 2 | Remplacer chaque `_____` par la bonne instruction |
| `api/Dockerfile` | 4 | Écrire, sous chaque commentaire, l'instruction correspondante |
| `api/.dockerignore` | 4 | Lister les fichiers à ne pas copier dans l'image |
| `db/Dockerfile` | 5 | Partir de l'image officielle de MariaDB et y ajouter les scripts et les données |
| `compose.yaml` | 6 | Décrire les services `db` et `api`, leur volume et leur ordre de démarrage |
| `train/Dockerfile`, `train/.dockerignore` | 8 | Les écrire, d'après le cahier des charges du cours |
| `compose.yaml`, `api/requirements.txt` | 8 | Ajouter le service `train` et brancher le modèle sur l'API |

Vous n'avez pas besoin de modifier les autres fichiers.

## Les programmes fournis

| Programme | Lancement | Configuration (variables d'environnement) |
|---|---|---|
| `api/main.py` | `uvicorn main:app --host 0.0.0.0 --port 8000` | `DB_HOST`, `DB_PORT`, `DB_USER`, `DB_PASSWORD`, `DB_NAME`, `MODEL_PATH` |
| `train/train.py` | `python train.py` | Les mêmes variables `DB_*`, et `MODEL_PATH` |

Le détail de chaque variable figure en tête de chaque programme. Une fois l'API lancée, sa documentation interactive est accessible à l'adresse `/docs`.

## Ressources

- Le [mémo Docker](https://drive.google.com/file/d/1zYblRINrIXSGXdlzFDao3YJ78pEcwL5r/view?usp=sharing) : un PDF de six fiches avec les commandes, les modèles de fichiers et les solutions aux erreurs les plus fréquentes.
- La documentation officielle de Docker : https://docs.docker.com
- La solution est publiée dans le dépôt [DS-Docker-Course-Solution](https://github.com/DataScientest/DS-Docker-Course-Solution/tree/fr) (branche `fr`) : c'est le projet final, tel qu'il doit être à la fin de l'étape 8. Utilisez-la pour comparer avec votre travail une fois une étape terminée, pas pour éviter de chercher.
