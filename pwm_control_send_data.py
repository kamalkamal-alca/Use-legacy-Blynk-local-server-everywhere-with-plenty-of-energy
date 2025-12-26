import BlynkLib
from BlynkTimer import BlynkTimer
import Adafruit_DHT, sys
import RPi.GPIO as GPIO

led1= 14
led2= 15
led3= 18
led4= 23
led5= 24
led6= 25
led7= 7
led8= 8

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(led1,GPIO.OUT)
GPIO.setup(led2,GPIO.OUT)
GPIO.setup(led3,GPIO.OUT)
GPIO.setup(led4,GPIO.OUT)
GPIO.setup(led5,GPIO.OUT)
GPIO.setup(led6,GPIO.OUT)
GPIO.setup(led7,GPIO.OUT)
GPIO.setup(led8,GPIO.OUT)

led9= 12
GPIO.setup(led9,GPIO.OUT)
p = GPIO.PWM(led9,100)         
p.start(0)   

BLYNK_AUTH_TOKEN ='CNWvcPHw3oVf1kgRJpHZwxINO4W66ICI'

timer = BlynkTimer()
x = 20
# Initialize Blynk
blynk = BlynkLib.Blynk(BLYNK_AUTH_TOKEN,server="192.168.2.101",port=8080)
    
def read_tempC():
    humidity, temperature = Adafruit_DHT.read_retry(11, 27)
    if humidity is not None and temperature is not None:
        print(temperature)
        print(humidity)
        blynk.virtual_write(9, temperature,)
        blynk.virtual_write(10, humidity)
        return temperature 
timer.set_interval(5, read_tempC) 
#================================================
@blynk.VIRTUAL_WRITE(0)
def my_write_handler(value):
#    global led_switch
    if int(value[0]) ==1:
        GPIO.output(led1, GPIO.HIGH)
        print('LED1 HIGH')
    else:
        GPIO.output(led1, GPIO.LOW)
        print('LED1 LOW')
#================================================
@blynk.VIRTUAL_WRITE(1)
def my_write_handler(value):
#    global led_switch
    if int(value[0]) ==1:
        GPIO.output(led2, GPIO.HIGH)
        print('LED2 HIGH')
    else:
        GPIO.output(led2, GPIO.LOW)
        print('LED2 LOW')
#================================================
@blynk.VIRTUAL_WRITE(2)
def my_write_handler(value):
    if int(value[0]) ==1:
        GPIO.output(led3, GPIO.HIGH)
        print('LED3 HIGH')
    else:
        GPIO.output(led3, GPIO.LOW)
        print('LED3 LOW')
#================================================
@blynk.VIRTUAL_WRITE(3)
def my_write_handler(value):
    if int(value[0]) ==1:
        GPIO.output(led4, GPIO.HIGH)
        print('LED4 HIGH')
    else:
        GPIO.output(led4, GPIO.LOW)
        print('LED4 LOW')
#================================================
@blynk.VIRTUAL_WRITE(4)
def my_write_handler(value):
    if int(value[0]) ==1:
        GPIO.output(led5, GPIO.HIGH)
        print('LED5 HIGH')
    else:
        GPIO.output(led5, GPIO.LOW)
        print('LED5 LOW')
#================================================
@blynk.VIRTUAL_WRITE(5)
def my_write_handler(value):
    if int(value[0]) ==1:
        GPIO.output(led6, GPIO.HIGH)
        print('LED6 HIGH')
    else:
        GPIO.output(led6, GPIO.LOW)
        print('LED6 LOW')
#================================================
@blynk.VIRTUAL_WRITE(6)
def my_write_handler(value):
    if int(value[0]) ==1:
        GPIO.output(led7, GPIO.HIGH)
        print('LED7 HIGH')
    else:
        GPIO.output(led7, GPIO.LOW)
        print('LED7 LOW')
#================================================
@blynk.VIRTUAL_WRITE(7)
def my_write_handler(value):
    if int(value[0]) ==1:
        GPIO.output(led8, GPIO.HIGH)
        print('LED8 HIGH')
    else:
        GPIO.output(led8, GPIO.LOW)
        print('LED8 LOW')
#================================================
@blynk.VIRTUAL_WRITE(8)
def my_write_handler(value):
    p.ChangeDutyCycle(float(value[0]))
    print(value)

while True:
    blynk.run()
    timer.run()  
