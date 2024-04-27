
# Documentation du Projet

## Vue d'ensemble
Cette documentation fournit un aperçu des scripts Python et des fonctionnalités au sein des dossiers "API_bourses" et "API_crypto".

## Documentation API_bourses

### connection.py
- **Description :** Établit une connexion MongoDB en utilisant des variables d'environnement. Définit les symboles boursiers.
- **Fonctionnalités :**
  - Récupère les détails de connexion à partir des variables d'environnement.
  - Initialise le client MongoDB et teste la connexion.
  
### delete_data.py
- **Description :** Gère la suppression des données dans MongoDB.
- **Fonctionnalités :**
  - Supprime des données basées sur des critères spécifiés.

### insert_data.py
- **Description :** Gère l'insertion de données dans MongoDB.
- **Fonctionnalités :**
  - Insère de nouvelles données dans la collection spécifiée.

### read_data.py
- **Description :** Permet la lecture de données depuis MongoDB.
- **Fonctionnalités :**
  - Lit et exporte éventuellement des données vers différents formats.

### update_data.py
- **Description :** Met à jour les données dans MongoDB en utilisant des données financières récupérées via une API.
- **Fonctionnalités :**
  - Met à jour la base de données avec des informations financières récentes.

## Documentation API_crypto

### connection_crypto.py
- **Description :** Établit une connexion MongoDB pour la gestion des données cryptographiques.
- **Fonctionnalités :**
  - Se connecte à MongoDB et liste les symboles de cryptomonnaies.

### delete_data_crypto.py
- **Description :** Gère la suppression des données de cryptomonnaie dans MongoDB.
- **Fonctionnalités :**
  - Supprime tous les documents dans une collection spécifiée et rapporte le nombre.

### insert_data_crypto.py
- **Description :** Insère des données de cryptomonnaie dans MongoDB.
- **Fonctionnalités :**
  - Insère des données historiques pour diverses cryptomonnaies récupérées via yfinance.

### read_data_crypto.py
- **Description :** Facilite la lecture des données de cryptomonnaie depuis MongoDB.
- **Fonctionnalités :**
  - Lit les données de la base de données.

### update_data_crypto.py
- **Description :** Met à jour les données de cryptomonnaie dans MongoDB.
- **Fonctionnalités :**
  - Mise à jour quotidienne de la base de données avec les derniers prix.

## Autres Fichiers

### data_bourses.py
- **Description :** Application Streamlit pour la visualisation des données financières.
- **Fonctionnalités :**
  - Fournit des onglets interactifs pour visualiser et analyser les données boursières et de cryptomonnaies.

### portefeuille.py
- **Description :** Application Streamlit pour l'analyse de portefeuille.
- **Fonctionnalités :**
  - Analyse les performances d'investissement basées sur des dates de début sélectionnées par l'utilisateur.

## Conclusion
Cette documentation complète vise à fournir des détails clairs et concis sur chaque partie du projet, améliorant la compréhension et facilitant les développements futurs.
