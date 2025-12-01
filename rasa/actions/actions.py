# Rasa custom actions stub
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionSuggestCareer(Action):
    def name(self) -> Text:
        return "action_suggest_career"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Replace with logic that queries your ML model or DB
        dispatcher.utter_message(text='Try Data Analyst, Software Engineer, Product Manager')
        return []
