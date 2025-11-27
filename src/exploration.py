import pandas as pd
import numpy as np

# Étape 1 : Exploration et compréhension des données (EDA)

# définition des types (optimisation mémoire)
dtype = {
    "Id": "int32",
    "gaming_interest_score": "float32",
    "insta_design_interest_score": "float32",
    "football_score": "float32",
    "recommended_product": "category",
    "campaign_success": "object",
    "age": "float32",
    "canal_recommande": "category"
}

# charger le CSV ( les données ) 
df = pd.read_csv("data/result.csv", sep=";", dtype=dtype)

# aperçu rapide du dataset
print("\n--- 5 premières lignes ---")
print(df.head())

# infos sur le dataset (types, valeurs manquantes, mémoire)
print("\n--- Informations dataset ---")
print(df.info())

# stats descriptives pour les colonnes numériques
print("\n--- Statistiques descriptives ---")
print(df.describe())
