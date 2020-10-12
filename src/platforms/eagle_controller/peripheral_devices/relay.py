import sys
sys.path.insert(0, "../../../../libs/")
sys.path.insert(0, "../../../../libs/isom/python")
sys.path.insert(0, "../../../../libs/hbt")
sys.path.insert(0, "../../../../src/")
# print(sys.path)
from core.device import Device
#from Device.CDevice import CDevice
import sparkplug_b as sparkplug
from sparkplug_b import *
import Cameras_pb2 as isom_cameras
import CodecDetails_pb2 as isom_codecdetails
from Cameras_pb2 import *
from CodecDetails_pb2 import *
from hbt_pb2 import *
from common.aliasmap import AliasMap



    
class RelayDevice(Device):

    def __init__(self, groupId, nodeId, deviceId):
        super().__init__(groupId, nodeId, deviceId)

    def getBirthCert(self,deviceMap,payload):

        payload = self.getPayload()

        addMetric(payload, "Events/RelayOn", AliasMap.Arm_Disarm_event, MetricDataType.Boolean, False)
        addMetric(payload, "Events/RelayOff", AliasMap.Fire_event, MetricDataType.Boolean, False)

        return payload

    def getDeathcert(self):
        print("Device Death certificates issued")
        
    def subsEvent(self):
        print("Device Event Subscribed")

    def  execCmd(self):
        print("Device Command executed")
