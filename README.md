# 📊 Analyse des Cibles – Projet EDA

Projet d'analyse exploratoire de données (EDA) visant à transformer des données brutes en informations exploitables pour anticiper les comportements utilisateurs lors de campagnes de sensibilisation au phishing.

**Équipe :** Bentifraouine Imène & Lyam Matic  
**Institution :** Escen — Bachelor Web & Technologies  
**Année académique :** 2025/2026  
**Date de remise :** 06 décembre 2025

## 🛠️ Installation & Pré-requis

### 1. Cloner le projet
```bash
git clone https://github.com/ton-repo/analyse-cibles.git
cd analyse-cibles
```

### 2. Installer l'environnement Python
```bash
python3 -m venv venv
source venv/bin/activate       # macOS / Linux
venv\Scripts\activate.bat      # Windows
```

### 3. Installer les dépendances
```bash
pip install -r requirements.txt
```

---

## ▶️ Exécution du script
```bash
python3 src/exploration.py
```

---

## 📊 Méthodologie

### 1. Import & Optimisation
- Types de données optimisés (`int32`, `float32`, `category`)
- Réduction mémoire : 0.04 Mo → 0.02 Mo

### 2. Nettoyage
- Suppression des doublons
- Suppression des valeurs manquantes
- Standardisation des colonnes

### 3. Détection d'anomalies (Z-score)

**Formule :** `Z = (x - μ) / σ`  
**Critère :** `|Z| > 3` = anomalie

**Résultats :**
- gaming_interest_score : 5 anomalies
- insta_design_interest_score : 2 anomalies
- football_interest_score : 2 anomalies
- **Dataset final :** 506 lignes

### 4. Analyse statistique

**KPI calculés :**
- Taux de réussite global : **69%**
- Par produit : Fifa (71%), Fortnite (70%), Instagram Pack (66%)
- Par canal : Facebook (85%), Mail (66%), Instagram (62%)
- Par âge : 45-60 ans (76%)

### 5. Datatelling

**Exemple :**  
Utilisateur de 25 ans, fan de Fifa/Fortnite, sur Facebook → **Taux de succès > 70%**

---

## 🎯 Résultats clés

- Les **18-60 ans** sont les plus sensibles
- **Facebook et Mail** sont les canaux les plus efficaces
- La **personnalisation** augmente significativement le taux de réussite

---

## 🛠️ Technologies

Python • Pandas • NumPy • Matplotlib 
