# Rasa Bot

## Comment lancer

*J'utilise un double environnement (Python/Anaconda) pour le lancer sur mon Mac M1.*

Pour lancer et utiliser le bot Rasa sur votre espace de travail Slack, suivez ces étapes :

1. Lancez le serveur Rasa :
    ```bash
    rasa run --port 5002 --connector slack --credentials credentials.yml --endpoints endpoints.yml --cors * --debug
    ```

2. Démarrez le serveur d'action :
    ```bash
    rasa run action
    ```

3. Lancez un serveur ngrok local pour exposer un webhook :
    ```bash
    ngrok http 5002
    ```
   Cette étape est nécessaire pour les webhooks.

---


