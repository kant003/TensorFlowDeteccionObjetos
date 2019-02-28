# importamos la libreria GPIO
#import RPi.GPIO as GPIO
# desactivamos mensajes de error
#GPIO.setwarnings(False)
# indicamos el uso de  la identificacion BCM para los GPIO
#GPIO.setmode(GPIO.BCM)
# indicamos que el GPIO18 es de salida de corriente
#GPIO.setup(18,GPIO.OUT)
# damos corriente al pin
#GPIO.output(18, True)
#GPIO.output(18, False)


import RPi.GPIO as GPIO
import time

servoPIN = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)

p = GPIO.PWM(servoPIN, 50) # GPIO 17 for PWM with 50Hz
p.start(2.5) # Initialization



def SetAngle(angle):
	duty = angle / 18 + 2
	GPIO.output(servoPIN, True)
	p.ChangeDutyCycle(duty)
	time.sleep(1)
	GPIO.output(servoPIN, False)
	p.ChangeDutyCycle(0)  

try:
  while True:
    SetAngle(90) 
    time.sleep(1)
    SetAngle(90)
    time.sleep(20000)
    SetAngle(20)
except KeyboardInterrupt:
  p.stop()
  GPIO.cleanup()

