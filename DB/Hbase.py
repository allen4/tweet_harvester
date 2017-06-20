"""Hbase database class"""
from DB.Database import Database
import happybase

class Hbase(Database):
    "Hbase database class"
    def __init__(self, host, table, column_family, port=None):
        Database.__init__(self, host, port)
        self.connection = self.connect()
        self.table = self.connection.table(table)
        self.column_family = column_family

    def store(self, json):
        'override the super function'

        # check if the tweet has already existed
        row = self.table.row(json['id_str'])
        if row:
            return
        json = self.parse_json(json, self.column_family)
        row_key_column = self.column_family + ':id_str'
        row_key = json[row_key_column]
        del json[row_key_column]

        self.table.put(row_key, json)

    def connect(self):
        'overide the super class function'
        #todo: enable to set port number
        connection = happybase.Connection(self.host, autoconnect=False)
        connection.open()
        return connection

    def disconnect(self):
        'overide the super class function'

    def parse_json(self, json_object, column_family=''):
        """Flatten the json object to level key value pair"""
        out = {}

        def flatten(tree_node, name=column_family):
            """Recursive function to traverse the json object"""
            if isinstance(tree_node, dict):
                for sub_tree_node in tree_node:
                    flatten(tree_node[sub_tree_node], name + sub_tree_node + '.')
            elif isinstance(tree_node, list):
                i = 0
                for sub_tree_node in tree_node:
                    flatten(sub_tree_node, name + str(i) + '.')
                    i += 1
            else:
                if isinstance(tree_node, basestring):
                    out[name[:-1]] = tree_node
                else:
                    out[name[:-1]] = unicode(tree_node)
        flatten(json_object)

        return out
