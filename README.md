# Projet N4 — Analyse de cibles (Traitement & Visualisation des données)

## 🔍 1. Exploration et compréhension

### 1. Importation et inspection


▪ Optimiser les performances lors de l’import :

- Nous avons identifié que les données étaient séparées par ;, ce qui empêchait un import correct.

- Nous avons défini des types  explicite (int32, float32, category, bool) dans l'objectif de réduire l’usage mémoire et accélérer les opérations futures.

1️⃣ Id (int32) : Identifiant unique de chaque personne.
2️⃣ gaming_interest_score (float32) : Intérêt pour les jeux vidéo.
3️⃣ insta_design_interest_score (float32) : Intérêt pour les vidéos de design sur Instagram.
4️⃣ football_score (float32) : Intérêt pour le football.
5️⃣ recommended_product (category) : Produit recommandé pour le phishing.
6️⃣ campaign_success (object) : Si la campagne de phishing a réussi ou non.
7️⃣ age (float32) : Âge de la personne.
8️⃣ canal_recommande (category) : Support utilisé pour le phishing (Email, Instagram…).

▪ Opignon sur la qualité de la donnée et de sa pertinence ?

- Une fois le séparateur appliqué, les données semblent bien structurées. Les colonnes contiennent des valeurs significatives pour les modéliser par la suite.

- Toutefois, une vérification est nécessaire afin de corriger les erreurs de type ou les données faussées (ex: valeurs aberrantes, type de campaign_success).


### 2. Nettoyage et mise en forme
