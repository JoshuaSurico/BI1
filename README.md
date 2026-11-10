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

Dans le cadre d'un projet ETL/BI en microservices, le choix de la stack s'est orienté vers **Python 3.14 + FastAPI** pour les raisons suivantes :

| Critère | FastAPI / Python | Express / Node.js (Alternative) | Justification |
| :--- | :--- | :--- | :--- |
| **Pertinence BI / ETL** | ⭐⭐⭐⭐⭐ (Standard de l'industrie) | ⭐⭐⭐ | Python dispose de l'écosystème data le plus riche (Pandas, Polars, DuckDB, SQLAlchemy). |
| **Swagger / OpenAPI** | **Natif & Automatique** | Requiert `tsoa` / plugins tiers | FastAPI génère la spec OpenAPI 3.1 sans aucune configuration ni étape de build. |
| **Typage & Validation** | Modèles Pydantic V2 | TypeScript + Décorateurs | Typage strict à l'exécution et sérialisation JSON haute performance (moteur Rust). |
| **Moteur de test** | Pytest + `httpx2` | Jest + Supertest | Tests légers, asynchrones, exécutables en une commande avec couverture fonctionnelle. |

### 🔗 Ressources & Liens étudiés pour la mise en place :
* **12 Factor App** : [The Twelve-Factor App Methodology](https://12factor.net/)
* **FastAPI Core & Routage** : [Documentation officielle FastAPI](https://fastapi.tiangolo.com/)
* **Bonnes pratiques d'architecture FastAPI** : [FastAPI Best Practices Guide](https://github.com/zhanymkanov/fastapi-best-practices)
* **Validation de schémas (Pydantic V2)** : [Pydantic V2 Documentation](https://docs.pydantic.dev/latest/)
* **Gestion moderne des settings** : [Pydantic Settings & ConfigDict](https://docs.pydantic.dev/latest/concepts/pydantic_settings/)
* **Moteur de test Pytest** : [Pytest Documentation](https://docs.pytest.org/en/stable/)
* **Configuration Debugging dans VS Code** : [VS Code Python Debugging Guide](https://code.visualstudio.com/docs/python/debugging)

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