# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionPizzaPrder(Action):

    def name(self) -> Text:
        return "action_confirm_order"

    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        pizza_quantity = tracker.get_slot('pizza_quantity')
        pizza_type = tracker.get_slot('pizza_type')
        pizza_size = tracker.get_slot('pizza_size')

        dispatcher.utter_message(text=f"Okay. You have ordered {pizza_quantity} {pizza_type} Pizza of {pizza_size} size. Please confirm the order.")


        return []
