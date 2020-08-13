import time 
import logging

template = {
    'events': [
        {
            'event': 'bot'
        }
    ],
    'responses': []
}

def findAnswer(qid, db):
    '''
    Search best answer (answer with best ranking) 
    Params:
        qid: question index
        db: sqlalchemy db instance
    '''
    ans = db.session.execute('select * from get_answer({})'.format(qid)).fetchone()
    if ans:
        return dict(ans)
    return None

def unableToAnswer(q):
    '''
    return response json object in case no answer can be found
    '''
    return {
        'text': "Je peux pas trouver une bonne réponse",
        'custom': {
            'type': 'unableToAnswer',
            'original_question': q
        }
    }

class ActionAnswerQuestion(object):
    def name(self):
        '''
            returns Action Name
        '''
        return 'action_answer_question'

    def run(self, tracker, es, db):
        '''
            execute Action
        '''
        st = time.time()
        # copy the template
        msg = template.copy()
        # get student's question
        question = tracker['latest_message']['text']
        # find similar questions
        similar_qs = es.findSimQuestions(question, 5)
        # if there's a good match (similarity > 80%)
        if similar_qs and similar_qs[0]['score'] > 1.8:
            match_id = similar_qs[0]['id']
            # find the corresponding answer of the best match
            ans = findAnswer(match_id, db)
            # if exists
            if ans:
                res = {
                    'text': "Voici une réponse intéressante",
                    'custom': {
                        'type': 'answer',
                        'answer': ans,
                        'original_question': question
                    }
                }
            # otherwise
            else:
                res = unableToAnswer(question)
        else:
            res = unableToAnswer(question)
        msg['responses'] = [res]
        logging.info('answer-duration %.2f' % (time.time() - st))
        return msg

class ActionDefaultFallback(object):

    def name(self):
        return 'action_default_fallback'

    def run(self, tracker, es, db):
        # copy the template
        msg = template.copy()
        msg['responses'] = [
            {
                'text': 'merci de re-poser la question',
                'custom': {
                    'type': 'chat'
                }
            }
        ]
        return msg
            
class ActionAsk2RateAnswer(object):

    def name(self):
        return 'action_ask2rate_answer'

    def run(self, tracker, es, db):
        # copy the template
        msg = template.copy()
        msg['responses'] = [
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
        return msg
            






