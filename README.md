🛠️ Installation & Pré-requis
1. Cloner le projet
git clone https://github.com/ton-repo/analyse-cibles.git
cd analyse-cibles

2. Installer l’environnement Python

Créer un environnement virtuel (optionnel mais recommandé) :

python3 -m venv venv
source venv/bin/activate  # macOS / Linux
venv\Scripts\activate.bat # Windows

3. Installer les dépendances
pip install -r requirements.txt

▶️ Exécution des scripts
Lancer l'exploration des données
python3 src/exploration.py

Lancer l’analyse statistique
python3 src/analyse_stats.py

📑 Structure du projet
analyse-cibles/
│
├── data/
│   └── dataset.csv
│
├── src/
│   ├── exploration.py
│   ├── analyse_stats.py
│   └── datatelling.py
│
├── outputs/
│   ├── graphiques/
│   ├── rapports/
│   └── anomalies.csv
│
└── README.md

📈 Méthodologie d’analyse
🔍 Exploration initiale

Vérification des données manquantes

Formatage des types (âge, dates, catégories produit…)

Suppression des doublons

🧹 Nettoyage

Correction des incohérences

Standardisation des valeurs textuelles

Filtrage des lignes erronées

📏 Détection des anomalies – Méthode Z-score

Nous avons utilisé le Z-score pour repérer les comportements atypiques :

Formule LaTeX :

Z = \frac{x - \mu}{\sigma}


Une valeur est considérée comme une anomalie si :

|Z| > 3

📊 Analyse statistique

Distribution par âge

Produits les plus performants

Canaux d’acquisition les plus efficaces

Taux de réussite par segment

🎯 Datatelling & interprétation

Traduction des chiffres en scénarios concrets, permettant de comprendre :

quels profils réagissent le mieux,

quelles stratégies marketing sont les plus efficaces,

quels segments sont sensibles à quelle sollicitation.