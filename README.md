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

### Mon choix : Python & FastAPI

#### Pourquoi ce choix ?
Durant mon CFC, je n'ai jamais eu de cours sur Python. J'ai donc profité de ce projet pour me lancer et découvrir ce langage. 

C'est une techno qui m'intéressait depuis un moment :
* La syntaxe a l'air simple et rapide à prendre en main.
* C'est ultra pratique à avoir dans sa boîte à outils : ça permet aussi bien de faire un petit script rapide pour dépanner que de développer des applications complètes.
* Beaucoup de choses fonctionnent directement sans devoir installer ou configurer des tonnes de trucs compliqués (« ça marche direct »).
* Pour un projet de BI et d'ETL, c'est idéal car Python est très utilisé pour tout ce qui touche à la manipulation de données.

#### Pourquoi FastAPI ?
J'ai choisi FastAPI comme framework web principalement pour deux raisons :
1. **La documentation Swagger automatique** : Contrairement à d'autres frameworks où il faut installer des plugins ou écrire la doc à la main, FastAPI s'occupe de tout tout seul sur `/docs`.
2. **La simplicité du code** : Il y a très peu de code à écrire pour exposer une route propre comme `/health`.

### 🔗 Ressources & Liens étudiés pour la mise en place :
* [Documentation officielle FastAPI](https://fastapi.tiangolo.com/) : prise en main du framework et création de la route `/health`.
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
├── .vscode/
│   └── launch.json          # Configuration du débogueur VS Code
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
├── .gitignore               # Exclusion venv, caches, fichiers temporaires
├── pytest.ini               # Résolution automatique du PYTHONPATH
├── requirements.txt         # Dépendances verrouillées
└── README.md                # Documentation projet & onboarding
```

---

## 3. Guide d'onboarding Développeur

Guide destiné à tout développeur intégrant le projet pour lancer l'environnement.

### Prérequis
* **Python 3.11+** (recommandé : 3.12, 3.13 ou 3.14)
* **Git**
* IDE supportant Python : **WebStorm** (avec plugin Python), **PyCharm**, ou **VS Code**

### Procédure d'installation

1. **Cloner le dépôt :**
   ```bash
   git clone git@github.com:JoshuaSurico/BI1.git
   cd BI1
   ```

2. **Créer et activer l'environnement virtuel :**
   * **Linux / macOS (Bash / Zsh) :**
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```
   * **Linux (Fish shell) :**
     ```fish
     python3 -m venv venv
     source venv/bin/activate.fish
     ```
   * **Windows (PowerShell) :**
     ```powershell
     python -m venv venv
     .\venv\Scripts\Activate.ps1
     ```

3. **Installer les dépendances :**
   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

4. **Démarrer le serveur de développement :**
   ```bash
   uvicorn app.main:app --reload --port 8000
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

Le moteur de test retenu est **Pytest**, couplé au `TestClient` FastAPI.

### Lancer la suite de tests
Assurez-vous que l'environnement virtuel est activé, puis exécutez :
```bash
pytest
```

### Détail du test implémenté (`tests/test_health.py`)
Le test valide de bout en bout :
1. Le code HTTP de réponse (`200 OK`).
2. Le respect du contrat de schéma (`status == "UP"` et `version == "1.0.0"`).
3. La présence obligatoire d'un horodatage ISO (`timestamp`).

---

## 6. Procédure de débogage & Points d'arrêt

Le bon fonctionnement du débogage pas-à-pas et l'interception sur point d'arrêt ont été validés dans **Visual Studio Code**.

### 1. Prérequis
* Installer l'extension officielle [Python pour VS Code](https://marketplace.visualstudio.com/items?itemName=ms-python.python) (qui installe et configure automatiquement l'extension [Python Debugger / debugpy](https://marketplace.visualstudio.com/items?itemName=ms-python.debugpy)).

### 2. Configuration (`.vscode/launch.json`)
Créer le fichier `.vscode/launch.json` à la racine :

```json
{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "Python: FastAPI Debug",
      "type": "debugpy",
      "request": "launch",
      "module": "uvicorn",
      "args": ["app.main:app", "--reload", "--port", "8000"],
      "jinja": true
    }
  ]
}
```

### 3. Tester le point d'arrêt
1. Sélectionner l'interpréteur de l'environnement virtuel : `Ctrl + Shift + P` > `Python: Select Interpreter` > `./venv/bin/python`.
2. Poser un point d'arrêt dans `app/api/health.py` sur la ligne retournant `HealthResponse`.
3. Lancer le débogueur avec la touche **`F5`** (ou menu *Run and Debug*).
4. Appeler l'API via le navigateur : [http://localhost:8000/health](http://localhost:8000/health).
5. **Résultat :** VS Code intercepte immédiatement la requête et suspend l'exécution sur votre point d'arrêt pour l'inspection des variables.

> Pour le détail complet des options de débogage et le troubleshooting, se référer au guide officiel : [VS Code Python Debugging Documentation](https://code.visualstudio.com/docs/python/debugging).