import pymongo
from pymongo import MongoClient

class MongoQueue(object):
    """docstring for MongoQueue"""
    def __init__(self, host='localhost', port=27017, database='mq', collection='queue'):
        super(MongoQueue, self).__init__()
        self.host = host
        self.port = port
        self.database = database
        self.collection = collection
        self.client = MongoClient(host, port)
        self.queue = self.client[database][collection]

    def enqueue(self, d):
        return self.queue.insert({'doc': d})

    def dequeue(self):
        d = self.queue.find_and_modify(query={}, sort={'_id': 1}, remove=True)
        if d:
            return d['doc']
        else: 
            return None

    def empty(self):
        return self.queue.find().count() == 0

if __name__ == '__main__':
    q = MongoQueue()
    map(lambda i: q.enqueue(i), range(0,5))
    while not q.empty():
        d = q.dequeue()
        if not d is None:
            print d
