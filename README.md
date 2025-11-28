1. Optimisation et import des données

Pour optimiser les performances lors de l’import du fichier CSV :

Les types des colonnes ont été définis explicitement (int32, float32, category) afin de réduire la mémoire utilisée par le dataset.

Cette optimisation permet à Pandas de stocker les données de manière plus compacte, surtout pour les grandes colonnes numériques et les colonnes catégorielles.

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

Première impression sur la qualité des données

Les données contiennent quelques doublons et des valeurs manquantes.

Certaines colonnes nécessitent d’être transformées en catégories pour réduire la mémoire.

La pertinence des données semble correcte : chaque colonne correspond à une information utile pour l’analyse et la modélisation.

2. Nettoyage et mise en forme
Étapes réalisées

Suppression des doublons : toutes les lignes identiques ont été retirées pour éviter des biais dans l’analyse.

Suppression des valeurs manquantes : toutes les lignes contenant des NaN ont été retirées pour garantir la cohérence du dataset.

Transformation des colonnes : certaines colonnes (campaign_success, recommended_product, canal_recommande) ont été converties en type category pour réduire la mémoire utilisée.

Justification des choix

Les doublons et valeurs manquantes peuvent fausser les statistiques et les modèles.

La transformation en category permet d’économiser de la mémoire tout en gardant les informations intactes.

Impact du nettoyage sur la mémoire
Moment	Mémoire utilisée
Avant nettoyage	0.04 Mo
Après suppression et transformation	0.02 Mo