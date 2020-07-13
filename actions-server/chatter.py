import grequests
import time
import random

exec_stack = []
nb_requests = 50

count = [0]

def log():
    count[0] += 1
    print(count[0])

for i in range(nb_requests):
    exec_stack.append(grequests.post('http://localhost:5005/webhooks/rest/webhook', json={
        "message":"c'est quoi html", 
        "sender": i
    }, hooks=dict(response=log)))

st = time.time()
grequests.map(exec_stack)
print('number of requests: %d - time-lapse: %.2f' % (nb_requests, time.time() - st))