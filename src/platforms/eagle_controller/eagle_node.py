import sys
sys.path.insert(0, "../../../libs/")
sys.path.insert(0, "../../../src/")
from core.node import Node
import sparkplug_b as sparkplug
from sparkplug_b import *

from http.server import HTTPServer, BaseHTTPRequestHandler
from threading import Thread
from platforms.eagle_controller.isom_event_handler import ISOMEventHandler

from functools import partial

class EagleNode(Node):

    def __init__(self, groupId, nodeId):
        super().__init__(groupId, nodeId)

    def getBirthCert(self):
        return self.getPayload()

    def getDeathcert(self):

        # Create the node death payload
        deathPayload = sparkplug.getNodeDeathPayload()
        #print(deathPayload)
        print("Node Death certificates issued")
        return deathPayload

    #@abstractmethod
    def subEvent(self):
        print("Node is subsribed to recieve events from the panel & attached devices")
        self.httpThread=Thread(target=self.httpServer)
        self.httpThread.start()

    def execCmd(self):
        print("Node command executed")

    def httpServer(self):
        print("Starting HTTP Server to handle ISOM Events")

        #TODO: Eagle Panel sends events to the direct address not to the localhost.
        #httpd = HTTPServer(('192.168.0.109', 5050), SimpleHTTPRequestHandler)

        #TODO: Hard coded 
        deviceId = 'Arming Station_11'

        handler = partial(ISOMEventHandler, deviceId, self.eventQueue)
        
        httpd = HTTPServer(('localhost', 5050), handler)
        httpd.serve_forever()
