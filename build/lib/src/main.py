import sys
import time
sys.path.insert(0, "../libs/")
sys.path.insert(0, "../src/")
#from apps.eagle_controller_app import msg_app
from http.server import HTTPServer, BaseHTTPRequestHandler
#from apps.http_handler import SimpleHTTPRequestHandler
from core.spg_engine import SPGEngine
from threading import Thread

from platforms.eagle_controller.peripheral_devices.ams import AMSDevice
from platforms.eagle_controller.peripheral_devices.relay import RelayDevice
from platforms.eagle_controller.eagle_node import EagleNode
from common.config import Config

if __name__ == "__main__":

    # Hardcoding Ids & Names, to be retrieved from the  platform discovery service
    # DeviceProps can also be retrieved from platform service and to be set to the below objects with enahancement in the APIs
    
    nodeId = 'Eagle Controller_1'
    deviceId = 'Arming Station_11'

    eagleNode = EagleNode(Config.groupId, nodeId)

    amsDevice = AMSDevice(Config.groupId,nodeId,deviceId)

    eagleNode.addDevice(deviceId, amsDevice)

    #SPGEngine currently handling single Node, but API can be extended to support multiple nodes    
    spgEngine = SPGEngine(eagleNode)

    spgEngine.start()
    
    
