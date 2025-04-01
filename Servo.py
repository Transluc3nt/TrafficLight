from gpiozero import LED
from gpiozero import PWMLED
from gpiozero import Servo
from time import sleep

max_correction=0.40
min_correction=0
maxPW=(2.0+max_correction)/1000
minPW=(1.0-min_correction)/1000
wave_servo = Servo(21,min_pulse_width=minPW,max_pulse_width=maxPW)

def wave(wave_data):
    print(wave_data)
    print(dir(wave_servo))
    while True:
        wave_servo.mid()
        print("mid", wave_servo.value)
        sleep(0.5)
        wave_servo.min()
        print("min", wave_servo.value)
        sleep(1)
        wave_servo.mid()
        print("mid", wave_servo.value)
        sleep(0.5)
        wave_servo.max()
        print("max", wave_servo.value)
        sleep(1)