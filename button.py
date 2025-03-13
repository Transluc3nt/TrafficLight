# import gpiozero
from gpiozero import LED
from gpiozero import Button
import time

print(dir(Button))

red_led = LED(3) # BCM GPIO3 = BOARD 5
red_button = Button(7,pull_up = True,bounce_time= None) 
while(True):
  if red_button.value == 1:
    print("Switch is pressed")
    red_led.on()
  else:
    print("Switch is not pressed")
    red_led.off()
  # Add a small delay if needed to avoid excessive CPU usage
  time.sleep(0.1)
