from machine import Pin
from time import sleep

botao = Pin(5, Pin.IN)

while True:
  leitura_botao = botao.value()
  print(leitura_botao)
  sleep(0.5)