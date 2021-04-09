from time import sleep
from machine import Pin, ADC

potentiometer = ADC(Pin(34))
potentiometer.width(ADC.WIDTH_10BIT)
potentiometer.atten(ADC.ATTN_11DB)

while True:
  potentiometer_value = potentiometer.read()
  print(potentiometer_value)

  sleep(0.1)