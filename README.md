# ChatBot Rasa - Gestion des Réservations

Ce projet implémente un chatbot pour la gestion des réservations d'un restaurant. Le chatbot permet de faire de nouvelles réservations, de supprimer des réservations existantes, de fournir des informations sur les réservations, et d'afficher le menu global, le menu du jour, ainsi que la liste des allergènes.

## Modifications pour respecter le chemin de conversation

### 1. `domain.yml`
Ce fichier définit les intentions, entités, actions, réponses et slots utilisés par le bot. Les modifications incluent :

- Ajout des intentions : `greet`, `new_reservation`, `delete_reservation`, `reservation_info`, `show_menu`, `show_allergen_list`, `provide_code`, `invalid_code`, `valid_code`.
- Définition des entités : `code`, `date`, `number_of_people`.
- Configuration des slots : `date`, `number_of_people`, `code`.
- Définition des réponses du bot pour chaque étape de la conversation.
- Déclaration des actions personnalisées : `action_send_summary`, `action_delete_reservation`.

### 2. `data/nlu.yml`
Ce fichier contient des exemples de phrases pour chaque intention afin d'entraîner le modèle NLU de Rasa. Les modifications incluent :

- Ajout des exemples de phrases pour chaque intention : `greet`, `new_reservation`, `delete_reservation`, `reservation_info`, `show_menu`, `show_allergen_list`.

### 3. `data/stories.yml`
Ce fichier décrit les différentes histoires que le bot doit suivre, en fonction des intentions détectées. Les modifications incluent :

- Ajout de nouvelles histoires pour gérer chaque chemin de conversation, incluant les étapes pour les intentions : `greet`, `new_reservation`, `delete_reservation`, `reservation_info`, `show_menu`, `show_allergen_list`.

### 4. `actions.py`
Ce fichier contient les actions personnalisées pour vérifier le code de réservation ou envoyer un résumé. Les modifications incluent :

- Ajout de l'action `ActionSendSummary` pour envoyer un résumé de la réservation.
- Ajout de l'action `ActionCheckCode` pour vérifier la validité d'un code de réservation.

## Lancer le projet

### Prérequis

- Python 3.10
- Rasa 3.1

### Installation

1. Clonez le repository :

    ```sh
    git clone https://github.com/votre-utilisateur/chatbot-rasa-reservations.git
    cd chatbot-rasa-reservations
    ```

2. Créez un environnement virtuel et activez-le :

    ```sh
    python -m venv venv
    source venv/bin/activate  # Pour Linux/Mac
    .\venv\Scripts\activate   # Pour Windows
    ```

3. Installez les dépendances :

    ```sh
    pip install rasa
    ```

### Entraîner le modèle

Pour entraîner le modèle Rasa, exécutez la commande suivante :

```sh
rasa train
