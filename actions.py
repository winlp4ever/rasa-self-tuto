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
            "type": "answer",
            "answer": "here is a very very long response :v"
        })
        return []

class ActionDefaultFallback(Action):

    def name(self):
        return 'action_default_fallback'

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(text="Merci de reposer la question")
        return []


class ActionAsk2RateAnswer(Action):
    def name(self):
        return "action_ask2rate_answer"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(
            text='how do you think about the response',
            json_message={
                "type": "multiple-choice",
                "choices": ""
            }
        )