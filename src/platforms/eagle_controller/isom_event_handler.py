import sys
import json
sys.path.insert(0, "../../libs/")
sys.path.insert(0, "../../src/")
from http.server import HTTPServer, BaseHTTPRequestHandler
import requests
from io import BytesIO
#from apps.eagle_controller_app import msg_app
#from apps.shareobj import *

from common.aliasmap import AliasMap

from sparkplug_b import *
from sparkplug_b_pb2 import Payload
import sparkplug_b as sparkplug

class ISOMEventHandler(BaseHTTPRequestHandler):

    def __init__(self, deviceId, eventQueue, *args, **kwargs):
        self.eventQueue = eventQueue
        self.deviceId =deviceId
        # BaseHTTPRequestHandler calls do_GET **inside** __init__ !!!
        # So we have to call super().__init__ after setting attributes.
        super().__init__(*args, **kwargs)

    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'Hello, world!')

    def parseAlarms(self, eventJson):

        eventList = eventJson['event']
        event = eventList[0]

        print(event)

        eventType = event['type']

        entityType = event['entityType']
        entityId = event['entityId']


        extensionList = event['extension']
        extension = extensionList[0]

        peripheralId = None
        dgTypeCategory = None
        partitionId = None 

        alarmType = None
        alarmState = False

        print("****eventType*****")
        print(eventType)

        if(eventType == "alarmState.alarm" or eventType == "alarmState.normal"):

            if(eventType == "alarmState.alarm"):
                alarmState = True
            elif(eventType == "alarmState.normal"):
                alarmState = False    

            if(entityType == "AC/DetectorGroups" and entityId == "1" ) :

                print("Entered in the If condition")

                peripheralId = extension['peripheralId']
                dgTypeCategory = extension['dgTypeCategory']
                partitionId = extension['partitionId']

                print(peripheralId)

                if(peripheralId == "1"):

                    if(dgTypeCategory == "MEDICAL"):
                        print("MEDICAL Alarm")
                        alarmType = AliasMap.Medical_Event

                    elif(dgTypeCategory == "FIRE"):
                        print("FIRE Alarm")
                        alarmType = AliasMap.Fire_Event

                    elif(dgTypeCategory == "BURGLARY"):
                        print("BURGLARY Alarm")                        
                        alarmType = AliasMap.Burglary_Event

        return alarmType, alarmState

    def do_POST(self):

        #self.deviceId = 'Arming Station_11'

        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        event_recieved = body.decode("utf-8")
        isom_event_recieved = json.loads(event_recieved)

        alarmType, alarmState = self.parseAlarms(isom_event_recieved)
        print(alarmType, alarmState)

        if (alarmType != None):

            if not self.eventQueue.full():
                
                alarm = { "deviceId": self.deviceId, "dataKey":alarmType, "dataValue": alarmState, "dataType": MetricDataType.Boolean }
                self.eventQueue.put( alarm )
  
        self.send_response(200)
        self.end_headers()
        response = BytesIO()
        response.write(b'This is POST request from server. ')
        response.write(b'Received: ')
        response.write(body)
        self.wfile.write(response.getvalue())
