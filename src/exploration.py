import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Étape 1 : Exploration et compréhension

# A Importation et inspection

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

# charger le CSV (les données)
df = pd.read_csv("data/result.csv", sep=";", dtype=dtype)

# aperçu rapide du dataset
print("\n--- 5 premières lignes ---")
print(df.head())

# infos sur le dataset (types, valeurs manquantes, mémoire)
print("\n--- Informations dataset ---")
print(df.info())

# Mémoire utilisée **avant nettoyage**
memoire_avant = df.memory_usage(deep=True).sum() / 1024**2  # en Mo
print(f"\nMémoire utilisée avant nettoyage : {memoire_avant:.2f} Mo")

# B Nettoyage et mise en forme

# stats descriptives pour les colonnes numériques
print("\n--- Statistiques descriptives ---")
print(df.describe())

# Nombre de doublons avant suppression
nb_doublons_avant = df.duplicated().sum()
print(f"\nNombre de doublons avant suppression : {nb_doublons_avant}")

# Afficher les doublons
if nb_doublons_avant > 0:
    print("\n--- Doublons avant suppression ---")
    print(df[df.duplicated(keep=False)])

# Supprimer les doublons
df = df.drop_duplicates()

# Vérification des valeurs manquantes
print("\n--- Valeurs manquantes par colonne ---")
print(df.isna().sum())

# Suppression des lignes avec valeurs manquantes
df = df.dropna()

# Transformation des colonnes, convertir en catégorie
df["campaign_success"] = df["campaign_success"].astype("category")

# Vérification des types après transformation
print("\n--- Types de colonnes après nettoyage ---")
print(df.dtypes)

# Mémoire utilisée après nettoyage
memoire_apres = df.memory_usage(deep=True).sum() / 1024**2
print(f"\nMémoire utilisée après nettoyage : {memoire_apres:.2f} Mo")

# Statistiques descriptives finales
print("\n--- Statistiques descriptives finales ---")
print(df.describe())

# Vérification finale des doublons
nb_doublons_final = df.duplicated().sum()
print(f"\nNombre de doublons après tout nettoyage : {nb_doublons_final}")

# Étape 2 : Détection d’anomalies

# Colonnes numériques sur lesquelles on cherche des anomalies
numeric_cols = [
    "gaming_interest_score",
    "insta_design_interest_score",
    "football_score",
    "age"
]

# --- Vérifier que les colonnes existent ---
numeric_cols = [col for col in numeric_cols if col in df.columns]

print("Colonnes utilisées pour la détection :", numeric_cols)

z_scores = (df[numeric_cols] - df[numeric_cols].mean()) / df[numeric_cols].std(ddof=0)
anomaly_z = (z_scores.abs() > 3)   # seuil classique : 3 écarts-types

print("\nAnomalies détectées (Z-score) :")
print(anomaly_z.sum())