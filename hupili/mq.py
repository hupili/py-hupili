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

    def size(self):
        return self.queue.find().count()

    def empty(self):
        return self.size() == 0

if __name__ == '__main__':
    import random
    q = MongoQueue()
    map(lambda i: q.enqueue(i), range(0,5))
    while not q.empty():
        print 'Remaining jobs:', q.size()
        d = q.dequeue()
        if not d is None:
            print 'Get Job:', d
            # Simulate job execution
            if random.random() > 0.5:
                print 'success'
            else:
                print 'fail'
                q.enqueue(d)

