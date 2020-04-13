# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


from typing import Any, Dict, List, Text
from rasa_sdk import Tracker, Action
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import UserUtteranceReverted

from rasa_sdk.forms import FormAction


class CovidForm(FormAction):
    '''Collects information then queries from api'''

    def name(self):
        return 'covid_form'

    @staticmethod
    def required_slots(tracker):
        return [
          'country',
        ]

    def slot_mappings(self) -> Dict[Text, Any]:
        return {
            'country': self.from_entity(
                entity='country',
                intent=[
                    'inform',
                    'ask_covid',
                ],
            ),
            'case_type': self.from_entity(
                entity='case_type',
                intent=[
                    'inform',
                    'ask_covid',
                ],
            ),
            'stat_type': self.from_entity(
                entity='stat_type',
                intent=[
                    'inform',
                    'ask_covid',
                ]
            )
        }

    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        country = tracker.get_slot('country')
        dispatcher.utter_message(
            f'Looks like you\'re trying to ask about covid-19 in {country}'
        )
        return []


class ActionGreet(Action):
    '''Revertible mapped action for utter_greet'''

    def name(self):
        return 'action_greet'

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(template='utter_greet')
        return [UserUtteranceReverted()]


class ActionBye(Action):
    '''Revertible mapped action for utter_bye'''

    def name(self):
        return 'action_bye'

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(template='utter_bye')
        return [UserUtteranceReverted()]


class ActionThank(Action):
    '''Revertible mapped action for utter_noworries'''

    def name(self):
        return 'action_thank'

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(template='utter_noworries')
        return [UserUtteranceReverted()]
