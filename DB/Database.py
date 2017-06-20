"""Common base class for all kinds of databases"""

class Database(object):
    'Common base class for all kinds of databases'
    def __init__(self, host, port=None):
        self.host = host
        self.port = port

    def connect(self):
        'connect to the database'
        pass

    def disconnect(self):
        'disconnect from the database'
        pass

    def store(self, json):
        'store the json to the database'
        pass

    def extra(self):
        'extra steps for child class'
        pass
