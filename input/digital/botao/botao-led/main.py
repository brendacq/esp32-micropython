from machine import Pin
from time import sleep

led = Pin(12, Pin.OUT)
botao = Pin(5, Pin.IN)

while True:
  led.value(botao.value())
  sleep(0.1)