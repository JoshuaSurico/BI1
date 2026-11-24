# BI1 - Template de Microservice ETL (FastAPI)

Template de base pour le développement d'un microservice au sein d'une architecture orientée microservices appliquée à un pipeline **ETL / Business Intelligence (BI)**.

---

## 📋 Table des matières
1. [Choix technologique & Justification](#1-choix-technologique--justification)
2. [Bonnes pratiques architecturales appliquées](#2-bonnes-pratiques-architecturales-appliquées)
3. [Guide d'onboarding Développeur](#3-guide-donboarding-développeur)
4. [Documentation Swagger & Spécification OpenAPI](#4-documentation-swagger--spécification-openapi)
5. [Tests fonctionnels](#5-tests-fonctionnels)
6. [Procédure de débogage & Points d'arrêt](#6-procédure-de-débogage--points-darrêt)

---

## 1. Choix technologique & Justification

### Mon choix : Python (PDM) & FastAPI

#### Pourquoi ce choix ?
Durant mon CFC, je n'ai jamais eu de cours sur Python. J'ai donc profité de ce projet pour me lancer et découvrir ce langage. 

C'est une techno qui m'intéressait depuis un moment :
* La syntaxe a l'air simple et rapide à prendre en main.
* C'est ultra pratique à avoir dans sa boîte à outils : ça permet aussi bien de faire un petit script rapide pour dépanner que de développer des applications complètes.
* Beaucoup de choses fonctionnent directement sans devoir installer ou configurer des tonnes de trucs compliqués (« ça marche direct »).
* Pour un projet de BI et d'ETL, c'est idéal car Python est très utilisé pour tout ce qui touche à la manipulation de données.
* Utilisation de **PDM** (gestionnaire de paquets moderne basé sur `pyproject.toml` et `pdm.lock`) pour garantir des installations reproductibles et des scripts centralisés (similaire à `npm` en Node.js).

#### Pourquoi FastAPI ?
J'ai choisi FastAPI comme framework web principalement pour deux raisons :
1. **La documentation Swagger automatique** : Contrairement à d'autres frameworks où il faut installer des plugins ou écrire la doc à la main, FastAPI s'occupe de tout tout seul sur `/docs`.
2. **La simplicité du code** : Il y a très peu de code à écrire pour exposer une route propre comme `/health`.

### 🔗 Ressources & Liens étudiés pour la mise en place :
* [Documentation officielle FastAPI](https://fastapi.tiangolo.com/) : prise en main du framework et création de la route `/health`.
* [Documentation officielle PDM](https://pdm-project.org/latest/) : gestion moderne des dépendances (`pyproject.toml`, lockfile, scripts).
* [FastAPI Best Practices Guide](https://github.com/zhanymkanov/fastapi-best-practices) : organisation et découpage des dossiers du projet.
* [The Twelve-Factor App](https://12factor.net/) : règles et bonnes pratiques pour concevoir des microservices.
* [Documentation Pydantic V2](https://docs.pydantic.dev/latest/) : validation des types et création du modèle de réponse.
* [Documentation Pydantic Settings](https://docs.pydantic.dev/latest/concepts/pydantic_settings/) : gestion centralisée des variables de configuration.
* [Documentation officielle Pytest](https://docs.pytest.org/en/stable/) : mise en place et exécution des tests fonctionnels.
* [Guide de débogage Python dans VS Code](https://code.visualstudio.com/docs/python/debugging) : configuration du fichier `launch.json` et des points d'arrêt.

---

## 2. Bonnes pratiques architecturales appliquées

Le projet suit les principes de la [**Twelve-Factor App**](https://12factor.net/) et du découpage modulaire :

```text
BI1/
├── .vscode/                 # (Local) Configuration IDE & débogueur VS Code
│   ├── launch.json
│   └── settings.json
├── app/
│   ├── __init__.py
│   ├── main.py              # Point d'entrée de l'application & configuration OpenAPI
│   ├── core/
│   │   ├── __init__.py
│   │   └── config.py        # Centralisation de la configuration (Pydantic BaseSettings)
│   └── api/
│       ├── __init__.py
│       └── health.py        # Contrôleur & contrat d'interface (Schéma Pydantic)
├── tests/
│   ├── __init__.py
│   └── test_health.py       # Tests fonctionnels de validation du healthcheck
├── .gitignore               # Exclusion .venv, caches, fichiers temporaires
├── pdm.lock                 # Arbre des dépendances verrouillé
├── pyproject.toml           # Configuration projet, dépendances & scripts PDM
├── pytest.ini               # Résolution automatique du PYTHONPATH
└── README.md                # Documentation projet & onboarding
```

---

## 3. Guide d'onboarding Développeur

Guide destiné à tout développeur intégrant le projet pour lancer l'environnement rapidement.

### Prérequis
* **Python 3.11+** (recommandé : 3.12, 3.13 ou 3.14)
* **PDM** ([Guide d'installation](https://pdm-project.org/latest/#installation))
* **Git**
* IDE supportant Python : **VS Code / VSCodium**, **PyCharm**, ou **WebStorm** (avec plugin Python)

### Procédure d'installation

1. **Cloner le dépôt :**
   ```bash
   git clone git@github.com:JoshuaSurico/BI1.git
   cd BI1
   ```

2. **Installer les dépendances (crée automatiquement le `.venv`) :**
   ```bash
   pdm install
   ```

3. **Démarrer le serveur de développement (avec hot-reload) :**
   ```bash
   pdm run dev
   ```
   L'API est immédiatement accessible sur `http://127.0.0.1:8000`.

---

## 4. Documentation Swagger & Spécification OpenAPI

FastAPI analyse les annotations de type et les modèles Pydantic pour générer la spécification **OpenAPI 3.1** à la volée.

Une fois le serveur démarré, deux interfaces de documentation interactive sont disponibles :
* **Swagger UI** : [http://localhost:8000/docs](http://localhost:8000/docs) (interface interactive permettant de tester les requêtes directement)
* **ReDoc** : [http://localhost:8000/redoc](http://localhost:8000/redoc) (vue orientée spécification technique)
* **Schéma JSON brut** : [http://localhost:8000/openapi.json](http://localhost:8000/openapi.json)

---

## 5. Tests fonctionnels

Le moteur de test retenu est **Pytest**, couplé au `TestClient` FastAPI et à `pytest-cov` pour la couverture de code.

### Lancer la suite de tests
* **Exécution standard :**
  ```bash
  pdm run test
  ```
* **Exécution avec rapport de couverture :**
  ```bash
  pdm run cov
  ```
* **Exécution en mode debug (ouvre `pdb` en cas d'échec) :**
  ```bash
  pdm run test-debug
  ```

### Détail du test implémenté (`tests/test_health.py`)
Le test valide de bout en bout :
1. Le code HTTP de réponse (`200 OK`).
2. Le respect du contrat de schéma (`status == "UP"` et `version == "1.0.0"`).
3. La présence obligatoire d'un horodatage ISO (`timestamp`).

---

## 6. Procédure de débogage & Points d'arrêt

Le débogage pas-à-pas fonctionne aussi bien **dans VS Code** que **directement dans le terminal**.

### Option A : Dans VS Code (Interface graphique)

1. Installer l'extension officielle [Python pour VS Code](https://marketplace.visualstudio.com/items?itemName=ms-python.python) (incluant `debugpy`).
2. Créer `.vscode/launch.json` à la racine :
   ```json
   {
     "version": "0.2.0",
     "configurations": [
       {
         "name": "FastAPI: Direct Launch",
         "type": "debugpy",
         "request": "launch",
         "module": "uvicorn",
         "args": ["app.main:app", "--port", "8000"],
         "jinja": true
       }
     ]
   }
   ```
3. Sélectionner l'interpréteur du `.venv` PDM : `Ctrl + Shift + P` > `Python: Select Interpreter` > `./.venv/bin/python`.
4. Poser un point d'arrêt dans `app/api/health.py` sur la ligne retournant `HealthResponse`.
5. Lancer le débogueur avec **`F5`**.
6. Appeler [http://localhost:8000/health](http://localhost:8000/health) : VS Code intercepte immédiatement la requête pour inspecter les variables.

### Option B : Dans le terminal (PDB natif)

1. Insérer `breakpoint()` à l'endroit souhaité dans votre code (ex: dans `app/api/health.py`).
2. Démarrer le serveur en mode debug (sans `--reload`) :
   ```bash
   pdm run debug
   ```
3. Appeler `http://127.0.0.1:8000/health` : le terminal bascule dans le débogueur interactif `(Pdb)` (`n` = ligne suivante, `p <var>` = afficher une variable, `c` = continuer).

> Pour le détail complet des options de débogage, se référer au guide officiel : [VS Code Python Debugging Documentation](https://code.visualstudio.com/docs/python/debugging).