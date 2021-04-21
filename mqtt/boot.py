import time
from mqtt import MQTTClient
import ubinascii
import machine
import micropython
import network
import esp
esp.osdebug(None)
import gc
gc.collect()

command = b'x' 
commandTime = 200 # em milisegundos 
commandLastTime = 0 


ssid = 'NOMEDAREDE'
password = 'SENHADAREDE'
mqtt_server = 'ENDEREÇO.IP'
server_port= 1883
# mqtt_user='user'
# mqtt_password='senha'

client_id = ubinascii.hexlify(machine.unique_id())
topic_sub = b'sub/msg'
topic_pub = b'pub/data'

last_message = 0
message_interval = 1
counter = 0

station = network.WLAN(network.STA_IF)

station.active(True)
station.connect(ssid, password)

while station.isconnected() == False:
  pass

print('Connection successful')
print(station.ifconfig())
