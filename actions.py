# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from rasa_sdk import Action
#
class ActionAnswerQuestion(Action):
#
    def name(self):
        return "action_answer_question"
#
    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(text='hmm now a response', json_message={
            "oof": "now what"
        })
        return []

class ActionDefaultFallback(Action):

    def name(self):
        return 'action_default_fallback'

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(text="Merci de reposer la question")
        return []