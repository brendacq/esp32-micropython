import time
from machine import Pin, ADC

led = Pin(2, Pin.OUT)
pot = ADC(Pin(34))

pot.width(ADC.WIDTH_10BIT)
pot.atten(ADC.ATTN_11DB)

def sub_cb(topic, msg):
  if topic == b'sub/msg' and msg == b'on':
    led.on()
  if topic == b'sub/msg' and msg == b'off':
    led.off()

def connect_and_subscribe():
  global client_id, mqtt_server, topic_sub, server_port, mqtt_user, mqtt_password
  client = MQTTClient(client_id, mqtt_server, server_port, mqtt_user, mqtt_password)
  client.set_callback(sub_cb)
  client.connect()
  client.subscribe(topic_sub)
  print('Connected to %s MQTT broker, subscribed to %s topic' % (mqtt_server, topic_sub))
  return client

def restart_and_reconnect():
  print('Failed to connect to MQTT broker. Reconnecting...')
  time.sleep(10)
  machine.reset()

try:
  client = connect_and_subscribe()
except OSError as e:
  restart_and_reconnect()
  

while True:
  try:
    client.check_msg()
    if (time.time() - last_message) > message_interval:
      # escrever no tópico pub/data
      pub_msg = str(pot.read())
      client.publish(topic_pub, pub_msg)
      last_message = time.time()

  except OSError as e:
    restart_and_reconnect()
