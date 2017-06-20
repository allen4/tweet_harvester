"""Couchdb database class"""
from DB.Database import Database
import couchdb

class Couchdb(Database):
    'Couchdb database class'
    def __init__(self, host, database, port="5984"):
        Database.__init__(self, host, port)
        self.server = self.connect()
        self.database = self.server[database]

    def connect(self):
        'Create the database connection'
        socket = 'http://' + self.host + ':' + self.port
        server = couchdb.Server(socket)
        return server

    def store(self, json):
        'override the super function'
        try:
            self.database.save(json)
        except Exception as e:
            if e.message[0] == "conflict":
                pass
            else:
                print e.message()
