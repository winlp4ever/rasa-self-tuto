import grequests
import time
import random

exec_stack = []
nb_requests = 1000
count = [0]

def log(r, *args, **kwargs):
    print(r.json()[0]['text'])

for i in range(nb_requests):
    exec_stack.append(grequests.post('http://localhost:5005/webhooks/rest/webhook', json={
        "message":"bonjour", 
        "sender": i
    }, hooks={'response': log}))

st = time.time()
grequests.map(exec_stack)
print('number of requests: %d - time-lapse: %.2f' % (nb_requests, time.time() - st))