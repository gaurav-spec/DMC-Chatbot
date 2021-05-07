# from typing import Any, Text, Dict, List, Union
# from rasa_sdk import Action, Tracker
# from rasa_sdk.events import SlotSet, EventType
# from rasa_sdk.executor import CollectingDispatcher
# from rasa_sdk.forms import FormAction
# #
# class ValidateRestaurantForm(Action):
#     def name(self) -> Text:
#         return "user_details_form"
#
#     @staticmethod
#     def run(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         required_slots = ["name", "number", "problem"]
#         print("required_slots(tracker: Tracker)")
#         return ["name", "number", "problem"]
#         # intent = tracker.latest_message['intent'].get('problem')
#         #           if intent == 'Drainage':
#         #               dispatcher.utter_message(response='utter_Drainage')
#         #           if intent == 'Electricity':
#         #              dispatcher.utter_message(response='utter_Electricity')
#         for slot_name in required_slots:
#             if tracker.slots.get(slot_name) is None:
#                 # The slot is not filled yet. Request the user to fill this slot next.
#                 return [SlotSet("requested_slot", slot_name)]
#
#     # All slots are filled.
#         return [SlotSet("requested_slot", None)]

#
# class ActionSubmit(Action):
#     def name(self) -> Text:
#         return "action_submit"
#
#     def run(
#             self,
#             dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         dispatcher.utter_message(template="utter_details_thanks",
#                                  Name=tracker.get_slot("name"),
#                                  mobile_number=tracker.get_slot("number"),
#                                  Problem=tracker.get_slot("problem"))
#         return []

# class ActionFormInfo(FormAction):
#     def name(self) -> Text:
#         """Unique identifier of the form"""
#         return "user_details_form"
#     @staticmethod
#     def required_slots(tracker: Tracker) -> List[Text]:
#         """A list of required slots that the form has to fill"""
#         return ["name", "number", "problem"]
#     def submit(
#             self,
#             dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any],
#     ) -> List[Dict]:
#         """Define what the form has to do
#             after all required slots are filled"""
#         # utter submit template
#         dispatcher.utter_message(template="utter_submit", Name=tracker.get_slot('name'),
#                                  mobile_number=tracker.get_slot('number'), Problem=tracker.get_slot("problem"))
#         return []
#     def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
#         """A dictionary to map required slots to
#             - an extracted entity
#             - intent: value pairs
#             - a whole message
#             or a list of them, where a first match will be picked"""
#         return {
#             "name": self.from_entity(entity="name", intent='my_name'),
#             "number": self.from_entity(entity="number", intent="mobile_number"),
#             "problem": self.from_entity(entity="problem", intent="problem")
#         }

# class ActionHelloWorld(FormAction):
#      def name(self) -> Text:
#          return "user_details_form"
#
#      @staticmethod
#      def required_slots(tracker: Tracker) -> List[Text]:
#
#          """A list of required slots that the form has to fill"""
#          print("required_slots(tracker: Tracker)")
#          return ["name", "number", "problem"]
#
#      def submit(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text: Any]) -> List[Dict]:
#          dispatcher.utter_message(template="utter_submit")
#
#          return []


from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet, EventType
from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []


class ActionCheck(Action):
    def name(self) -> Text:
        return "user_details_form"

    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # try:
        #     print(tracker.latest_message['intent'].get('name'))
        # except Exception as e:
        #     print(e)
        required_slots = ["name", "number", "problem"]
        intent = tracker.latest_message['intent'].get('problem')
        if intent == 'Drainage':
            dispatcher.utter_message(response='utter_Drainage')
        if intent == 'Electricity':
            dispatcher.utter_message(response='utter_Electricity')

        # return []

# class ActionCheckEveryday(Action):
#     def name(self) -> Text:
#         return "action_check_everyday"
#
#     def run(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         # try:
#         #     print(tracker.latest_message['intent'].get('name'))
#         # except Exception as e:
#         #     print(e)
        for slot_name in required_slots:
                if tracker.slots.get(slot_name) is None:
                     # The slot is not filled yet. Request the user to fill this slot next.
                     return [SlotSet("requested_slot", slot_name)]
        return [SlotSet("requested_slot", None)]

class ActionSubmit(Action):
     def name(self) -> Text:
         return "action_submit"

     def run(
             self,
             dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
         dispatcher.utter_message(template="utter_details_thanks",
                                  Name=tracker.get_slot("name"),
                                  mobile_number=tracker.get_slot("number"),
                                  Problem=tracker.get_slot("problem"))
         return []