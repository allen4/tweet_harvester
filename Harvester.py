"""
The harvester class
"""
import os.path
import json
from DB.Couchdb import Couchdb
from DB.Hbase import Hbase
from Config import Config

class Harvester(object):
    """Base class for tweet harvester"""
    def __init__(self):
        self.config = self.get_config()

    def get_config(self):
        'get the configuration json'
        config = Config()
        return config.get_config_all()

    def database_selector(self):
        'select the right database according to the config'
        database_config = self.config['config']['db']
        database_type = database_config['type'].lower()
        database_host = database_config['host']

        if database_type == 'hbase':
            if 'port' in database_config:
                database = Hbase(database_host,
                                 database_config['table'],
                                 database_config['column_family'],
                                 database_config['port']
                                )
            else:
                database = Hbase(database_host,
                                 database_config['table'],
                                 database_config['column_family']
                                )
        elif database_type == 'couchdb':
            database = Couchdb(database_host,
                               database_config['database'],
                               database_config['port']
                              )
        return database
