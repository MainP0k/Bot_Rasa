from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionSendSummary(Action):

    def name(self) -> Text:
        return "action_send_summary"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Logique pour récupérer le résumé de la réservation
        summary = "Résumé de votre réservation."
        dispatcher.utter_message(text=summary)
        return []


class ActionCheckCode(Action):

    def name(self) -> Text:
        return "action_check_code"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        code = tracker.get_slot('code')

        if code == "1234":  # Exemple de validation du code
            dispatcher.utter_message(template="utter_valid_code")
            return []
        else:
            dispatcher.utter_message(template="utter_invalid_code")
            return []


