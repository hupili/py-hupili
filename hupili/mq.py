import pymongo
from pymongo import MongoClient

client = MongoClient()
db = client.test
q = db.queue

def enqueue(d):
    return q.insert({'doc': d})

def dequeue():
    d = q.find_and_modify(query={}, sort={'_id': 1}, remove=True)
    if d:
        return d['doc']
    else: 
        return None

def empty():
    return q.find().count() == 0

map(lambda i: enqueue(i), range(0,5))

#print [i for i in q.find()]

while not empty():
    d = dequeue()
    if not d is None:
        print d
