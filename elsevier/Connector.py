from elsapy.elsclient import ElsClient
import json

class Connector:
    
    def __init__(self):
        self.client = self.connect()

    
    def connect(self):
        con_file = open("config.json")
        config = json.load(con_file)
        con_file.close()
        client = ElsClient(config['apikey'])
        return client
