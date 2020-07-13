from flask import Flask, render_template, jsonify, request
from flask_socketio import SocketIO, send, emit
from flask_sqlalchemy import SQLAlchemy

import json

from similarity_search import SimiSearch
from action_list import actions

sim = SimiSearch()
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = ""
db = SQLAlchemy(app)

@app.route('/bob-actions', methods=['POST'])
def respond():
    if request.headers['Content-Type'] == 'application/json':
        if request.json['next_action'] in actions:
            return actions[request.json['next_action']].run(request.json['tracker'], sim, db), 200


if __name__ == '__main__':
    app.run(port=5006, threaded=True)