"""
The stream tweet harvester class
"""
import json
from Harvester import Harvester
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

class StdOutListener(StreamListener):
    """The tweets stream listener"""

    def __init__(self, stream_harvester):
        super(StdOutListener, self).__init__()
        self.stream_harvester = stream_harvester
        self.database = stream_harvester.database_selector()

    def on_data(self, data):
        data_json = json.loads(data)
        self.database.store(data_json)

    def on_error(self, status):
        print status

class StreamHarvester(Harvester):
    """The stream tweet harvester"""

    def __init__(self, auth_index):
        Harvester.__init__(self)
        self.consumer_key = self.config['auth'][auth_index][0]
        self.consumer_secret = self.config['auth'][auth_index][1]
        self.access_token = self.config['auth'][auth_index][2]
        self.access_token_secret = self.config['auth'][auth_index][3]

        self.stream_listener = StdOutListener(self)

    def harvest(self):
        """Havest the stream tweets"""
        auth_object = OAuthHandler(self.consumer_key, self.consumer_secret)
        auth_object.set_access_token(self.access_token, self.access_token_secret)
        stream = Stream(auth=auth_object, listener=self.stream_listener)
        stream.filter(locations=self.config['config']['tweepy']['filter']['bounding_box'])
