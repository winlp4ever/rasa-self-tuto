from flask import Flask, render_template, jsonify, request

from flask_socketio import SocketIO, send, emit

from flask_sqlalchemy import SQLAlchemy

import json

actions = {
    'action_answer_question': {
        'events': [
            {
                'event': 'bot',
            }
        ],
        'responses': [
            {
                "text": 'here is a response',
                "custom": {
                    "type": 'answer',
                    "answer": {
                        "text": "this is a very very long response"
                    }
                }
            }
        ]
    },
    'action_default_fallback': {
        'events': [
            {
                'event': 'bot',
            }
        ],
        'responses': [
            {
                "text": 'please retype your question and make it more precise',
                "type": 'chat'
            }
        ]
    },
    'action_propose_relevant_questions': {
        'events': [
            {
                'event': 'bot',
            }
        ],
        'responses': [
            {
                "text": 'here is some questions that may interest you',
                'custom': {
                    "type": 'multiple-choices',
                }
            }
        ]
    },
    'action_ask2rate_answer': {
        'events': [
            {
                'event': 'bot',
            }
        ],
        'responses': [
            {
                "text": 'what do you think of the answer?',
                "custom": {
                    "type": 'multiple-choices',
                    "choices": [
                        1, 2
                    ]
                }
            }
        ]
    }
}

app = Flask(__name__)

@app.route('/bob-actions', methods=['POST'])
def respond():
    if request.headers['Content-Type'] == 'application/json':
        print(json.dumps(request.json['tracker']['latest_message']['text'], indent=4))
        if request.json['next_action'] in actions:
            return actions[request.json['next_action']], 200


if __name__ == '__main__':
    app.run(port=5006, threaded=True)