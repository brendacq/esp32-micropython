from machine import Pin
from time import sleep

botao = Pin(4, Pin.IN)

while True:
  print(botao.value())
  sleep(0.5)