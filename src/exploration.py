import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ============================================================
# 🔍 EXPLORATION & COMPRÉHENSION DES DONNÉES (EDA)
# ============================================================
print("\n=== PARTIE 1 : EXPLORATION & COMPRÉHENSION DES DONNÉES (EDA) ===")

# définition des types (optimisation mémoire)
dtype = {
    "Id": "int32",
    "gaming_interest_score": "float32",
    "insta_design_interest_score": "float32",
    "football_interest_score": "float32",
    "recommended_product": "category",
    "campaign_success": "object",
    "age": "float32",
    "canal_recommande": "category"
}

# Charger le CSV
df = pd.read_csv("data/result.csv", sep=";", dtype=dtype)

# Aperçu du dataset
print("\n--- 5 premières lignes ---")
print(df.head())

# Infos + mémoire avant nettoyage
print("\n--- Informations dataset ---")
print(df.info())

memoire_avant = df.memory_usage(deep=True).sum() / 1024**2
print(f"\nMémoire utilisée avant nettoyage : {memoire_avant:.2f} Mo")


# ============================================================
# 🧹 1. NETTOYAGE & PRÉPARATION DES DONNÉES
# ============================================================
print("\n=== PARTIE NETTOYAGE & OPTIMISATION MÉMOIRE ===")

# Suppression des doublons 
nb_doublons_avant = df.duplicated().sum()
print(f"\nNombre de doublons avant suppression : {nb_doublons_avant}")
df = df.drop_duplicates()

# Suppression des valeurs manquantes 
print("\nValeurs manquantes par colonne :")
print(df.isna().sum())
df = df.dropna()

# Nettoyage des colonnes catégorielles 
categorical_cols = ["recommended_product", "canal_recommande"]

for col in categorical_cols:
    df[col] = df[col].astype(str)  
    df[col] = df[col].str.strip().str.lower().str.replace(r'\s+', ' ', regex=True)
    df[col] = df[col].str.title()
    df[col] = df[col].astype("category") 

# Nettoyage campaign_success 
df["campaign_success"] = df["campaign_success"].astype(str).str.strip().str.lower()
df["campaign_success"] = df["campaign_success"].map({"true": True, "false": False})

# Vérification types et mémoire 
print("\nTypes après nettoyage :")
print(df.dtypes)

memoire_apres = df.memory_usage(deep=True).sum() / 1024**2
print(f"\nMémoire utilisée après nettoyage : {memoire_apres:.2f} Mo")

# Statistiques descriptives finales 
print("\nStatistiques descriptives finales :")
print(df.describe())

# Vérification des doublons finaux 
nb_doublons_final = df.duplicated().sum()
print(f"\nNombre de doublons après nettoyage : {nb_doublons_final}")


# ============================================================
# 🕵️ 2. DÉTECTION D’ANOMALIES (Z-SCORE)
# ============================================================
print("\n=== PARTIE 2 : DÉTECTION D’ANOMALIES (Z-SCORE) ===")

numeric_cols = [
    "gaming_interest_score",
    "insta_design_interest_score",
    "football_interest_score",
    "age"
]

categorical_cols = ["recommended_product", "canal_recommande"]

# Nettoyage standard des colonnes catégorielles
for col in categorical_cols:
    df[col] = df[col].astype(str).str.strip().str.lower()
    df[col] = df[col].str.replace(r'\s+', ' ', regex=True)
    df[col] = df[col].astype("category")

for col in categorical_cols:
    df[col] = df[col].str.title()

# Nettoyage campaign_success
print("\n--- Valeurs uniques dans campaign_success (avant nettoyage) ---")
print(df["campaign_success"].unique())

df["campaign_success"] = (df["campaign_success"].astype(str).str.strip().str.lower())
df["campaign_success"] = df["campaign_success"].map({"true": True, "false": False})

print("\n--- Valeurs uniques dans campaign_success (après nettoyage) ---")
print(df["campaign_success"].unique())

numeric_cols = [col for col in numeric_cols if col in df.columns]
print("Colonnes utilisées pour la détection :", numeric_cols)

# Calcul du Z-score
z_scores = (df[numeric_cols] - df[numeric_cols].mean()) / df[numeric_cols].std(ddof=0)
anomaly_z = (z_scores.abs() > 3)

print("\nAnomalies détectées (Z-score) :")
print(anomaly_z.sum())


# ============================================================
# 👁️‍🗨️ 2. VISUALISATION DES ANOMALIES
# ============================================================
print("\n=== PARTIE 2B : VISUALISATION DES ANOMALIES ===")

for col in numeric_cols:
    mean_val = df[col].mean()
    std_val = df[col].std(ddof=0)

    anomalies = anomaly_z[col]
    normal = ~anomalies

    plt.figure(figsize=(10, 4))

    plt.scatter(df.index[normal], df[col][normal], color='blue', alpha=0.7, label='Normal')
    plt.scatter(df.index[anomalies], df[col][anomalies], color='red', alpha=0.9, label='Anomalie')

    plt.axhline(mean_val, color='green', linestyle='--', linewidth=1.5, label='Moyenne')
    plt.axhline(mean_val + 3*std_val, color='orange', linestyle='--', linewidth=1.5, label='+3σ')
    plt.axhline(mean_val - 3*std_val, color='orange', linestyle='--', linewidth=1.5, label='-3σ')

    plt.title(f'Détection d\'anomalies pour {col}', fontsize=14)
    plt.xlabel('Index', fontsize=12)
    plt.ylabel(col, fontsize=12)
    plt.legend()
    plt.show()

# Dataset sans anomalies
df_clean = df[~anomaly_z.any(axis=1)]
print(f"\nNombre de lignes après suppression des anomalies : {df_clean.shape[0]}")


# ============================================================
# 📈 3. ANALYSE STATISTIQUE (KPI)
# ============================================================
print("\n=== PARTIE 3 : ANALYSE STATISTIQUE (KPI) ===")

df_stats = df_clean.copy()

print("\n===== ANALYSE STATISTIQUE =====")

# KPI 1 : taux global
success_rate = df_stats["campaign_success"].mean()
print(f"\nTaux de réussite global : {success_rate*100:.2f}%")

plt.figure(figsize=(5,5))
plt.bar(["Succès"], [success_rate])
plt.title("Taux de réussite global")
plt.ylabel("Taux")
plt.show()


# KPI 2 : réussite par produit
success_by_product = df_stats.groupby("recommended_product")["campaign_success"].mean()
print("\nTaux de réussite par produit :")
print(success_by_product)

success_by_product.plot(kind="bar", figsize=(7,5))
plt.title("Taux de réussite par produit")
plt.ylabel("Taux de réussite")
plt.show()


# KPI 3 : réussite par canal
success_by_channel = df_stats.groupby("canal_recommande")["campaign_success"].mean()
print("\nTaux de réussite par canal :")
print(success_by_channel)

success_by_channel.plot(kind="bar", figsize=(7,5))
plt.title("Taux de réussite par canal")
plt.ylabel("Taux de réussite")
plt.show()


# KPI 4 : réussite par âge (groupes)
df_stats["age_group"] = pd.cut(
    df_stats["age"],
    bins=[0, 18, 30, 45, 60, 99],
    labels=["<18", "18-30", "30-45", "45-60", "60+"]
)

success_by_age = df_stats.groupby("age_group")["campaign_success"].mean()
print("\nTaux de réussite par tranche d’âge :")
print(success_by_age)

success_by_age.plot(kind="bar", figsize=(7,5))
plt.title("Taux de réussite par âge")
plt.ylabel("Taux de réussite")
plt.show()


# ============================================================
# 🔗 4. MATRICE DE CORRÉLATION
# ============================================================
print("\n=== PARTIE 4 : MATRICE DE CORRÉLATION ===")

score_cols = [
    "gaming_interest_score",
    "insta_design_interest_score",
    "football_interest_score",
    "age"
]

corr = df_stats[score_cols + ["campaign_success"]].corr()

print("\n===== MATRICE DE CORRÉLATION =====")
print(corr)

plt.figure(figsize=(8,6))
plt.imshow(corr, cmap="coolwarm", interpolation="nearest")
plt.colorbar()
plt.title("Matrice de corrélation")
plt.xticks(range(len(corr)), corr.columns, rotation=45)
plt.yticks(range(len(corr)), corr.columns)
plt.show()
