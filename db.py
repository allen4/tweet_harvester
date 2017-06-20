"""The database class"""
import happybase

class Database(object):
    """The database class"""
    def __init__(self, host):
        self.host = host
        self.connection = self.db_con()

    def db_con(self):
        """Create the database connection for specified table"""
        connection = happybase.Connection(self.host, autoconnect=False)
        connection.open()
        return connection

    def db_table(self, table):
        """Get the database table from the database connection"""
        return self.connection.table(table)
