"""Get the configuration object from the configuration file"""
import os
import json

class Config(object):
    'the Config class'
    def __init__(self):
        self.basepath = os.path.dirname(__file__)
        self.auth_path = os.path.abspath(os.path.join(self.basepath, "config", "auths.txt"))
        self.config_path = os.path.abspath(os.path.join(self.basepath, "config", "config.json"))

    def get_config_all(self):
        'get the config object'
        if not os.path.isfile(self.auth_path):
            raise Exception("The auth file doesn't exist.")
        if not os.path.isfile(self.config_path):
            raise Exception("The configuration file doesn't exist.")

        # put all configuration into one single object
        config = {}
        config['auth'] = self.get_auth()
        config['config'] = self.get_config()
        return config

    def get_auth(self):
        """Get Twitter API authentication details"""
        auths = []
        with open(self.auth_path, 'r') as auth_file:
            for line in auth_file:
                auths.append(line.split())
        return auths

    def get_config(self):
        """Get the configuration data"""
        with open(self.config_path) as data_file:
            config = json.load(data_file)
        return config
