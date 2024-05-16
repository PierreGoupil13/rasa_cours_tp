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


## Explications techniques

J'ai préferé me concentrer sur le coté fonctionnel de rasa et j'ai donc laissé certaines choses non réalisés :
 1. Une gestion plus propre des dates
 2. Une gestion plus propres d'un envoie de mauvais code de réservations
 3. Toute les options possibles n'ont pas été implémentées (commentaires, modification, ..)
 4. La suppression est implémenter coté custom actions mais je n'ai pas fais de story

Il est possible de l'intégré avec slack.
Un story graph path ainsi qu'une vidéo de démo est disponible dans le repository.

## Conclusion

Ce projet fut très intéressant, avec plus de temps j'aurais voulu pousser plus loin le bot mais je pense avoir couvert une bonne partie des fonctionnalitées disponibles.


---


