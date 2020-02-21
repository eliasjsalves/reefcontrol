import RPi.GPIO as GPIO
import time

class Lamp:
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)

    #blue
    GPIO.setup(11,GPIO.OUT)
    #white
    GPIO.setup(13,GPIO.OUT)
    #red/uv
    GPIO.setup(15,GPIO.OUT)

    def __init__(self):

        self.blue_leds = GPIO.PWM(11,100)
        self.blue_leds.start(0)
        self.white_leds = GPIO.PWM(13,100)
        self.white_leds.start(0)
        self.red_leds = GPIO.PWM(15,100)
        self.red_leds.start(0)

    def turn_blue_to(self, intensity=0):
        self.blue_leds.ChangeDutyCycle(intensity)

    def turn_white_to(self, intensity=0):
        self.white_leds.ChangeDutyCycle(intensity)

    def turn_red_to(self, intensity=0):
        self.red_leds.ChangeDutyCycle(intensity)

