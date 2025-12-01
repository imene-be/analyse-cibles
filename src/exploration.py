import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ========================================
# 🔍 1. Exploration et compréhension
# ========================================

# A Importation et inspection

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

# ========================================
# 🕵 2. Détection d’anomalies
# ========================================

# Colonnes numériques à analyser
numeric_cols = [
    "gaming_interest_score",
    "insta_design_interest_score",
    "football_interest_score",
    "age"
]

# 🔹 Nettoyage des colonnes pour éviter les doublons invisibles
categorical_cols = ["recommended_product", "canal_recommande"]

for col in categorical_cols:
    df[col] = df[col].astype(str).str.strip().str.lower()
    df[col] = df[col].str.replace(r'\s+', ' ', regex=True)
    df[col] = df[col].astype("category")

# Ajout majuscule aux catégorie
for col in categorical_cols:
    df[col] = df[col].str.title()

# Conversion de campaign_success en booléen
print("\n--- Valeurs uniques dans campaign_success (avant nettoyage) ---")
print(df["campaign_success"].unique())

# Normalisation
df["campaign_success"] = (df["campaign_success"].astype(str).str.strip().str.lower())

# Conversion en booléen
df["campaign_success"] = df["campaign_success"].map({"true": True, "false": False})

print("\n--- Valeurs uniques dans campaign_success (après nettoyage) ---")
print(df["campaign_success"].unique())

# Vérifier que les colonnes existent réellement dans le dataset
numeric_cols = [col for col in numeric_cols if col in df.columns]
print("Colonnes utilisées pour la détection :", numeric_cols)

# Calcul des Z-scores
z_scores = (df[numeric_cols] - df[numeric_cols].mean()) / df[numeric_cols].std(ddof=0)

# Détection des anomalies : valeurs dont |Z-score| > 3
anomaly_z = (z_scores.abs() > 3)
print("\nAnomalies détectées (Z-score) :")
print(anomaly_z.sum())

# Visualisation
for col in numeric_cols:
    mean_val = df[col].mean()
    std_val = df[col].std(ddof=0)

    # Créer des masques
    anomalies = anomaly_z[col]
    normal = ~anomalies

    plt.figure(figsize=(10, 4))

    # Points normaux
    plt.scatter(df.index[normal], df[col][normal], color='blue', alpha=0.7, label='Normal')
    # Points anomalies
    plt.scatter(df.index[anomalies], df[col][anomalies], color='red', alpha=0.9, label='Anomalie')

    # Moyenne et bornes ±3σ
    plt.axhline(mean_val, color='green', linestyle='--', linewidth=1.5, label='Moyenne')
    plt.axhline(mean_val + 3*std_val, color='orange', linestyle='--', linewidth=1.5, label='+3σ')
    plt.axhline(mean_val - 3*std_val, color='orange', linestyle='--', linewidth=1.5, label='-3σ')

    # Titre et légende
    plt.title(f'Détection d\'anomalies pour {col}', fontsize=14)
    plt.xlabel('Index', fontsize=12)
    plt.ylabel(col, fontsize=12)
    plt.legend()
    plt.show()

# Supprimer les anomalies pour analyses futures
df_clean = df[~anomaly_z.any(axis=1)]
print(f"\nNombre de lignes après suppression des anomalies : {df_clean.shape[0]}")

# ========================================
# 📈 3. ANALYSE STATISTIQUE (KPI)
# ========================================

df_stats = df_clean.copy()

print("\n===== ANALYSE STATISTIQUE =====")

# Taux de réussite global
success_rate = df_stats["campaign_success"].mean()
print(f"\nTaux de réussite global : {success_rate*100:.2f}%")

plt.figure(figsize=(5,5))
plt.bar(["Succès"], [success_rate])
plt.title("Taux de réussite global")
plt.ylabel("Taux")
plt.show()


# Taux de réussite par produit recommandé
success_by_product = df_stats.groupby("recommended_product")["campaign_success"].mean()

print("\nTaux de réussite par produit :")
print(success_by_product)

success_by_product.plot(kind="bar", figsize=(7,5))
plt.title("Taux de réussite par produit")
plt.ylabel("Taux de réussite")
plt.show()


# Taux de réussite par canal
success_by_channel = df_stats.groupby("canal_recommande")["campaign_success"].mean()

print("\nTaux de réussite par canal :")
print(success_by_channel)

success_by_channel.plot(kind="bar", figsize=(7,5))
plt.title("Taux de réussite par canal")
plt.ylabel("Taux de réussite")
plt.show()


# Taux de réussite par tranche d’âge
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


# Corrélation entre scores d’intérêt et réussite
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

# ========================================
# 4. Datatelling et création de l’attaque
# ========================================

