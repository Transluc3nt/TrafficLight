from gpiozero import LED
import time

red_led = LED(3)
yellow_led = LED(4)
green_led = LED(5)

def stop_light(traffic_status):
    print(traffic_status)
    red,yellow,green = traffic_status
    print(traffic_status[red])
    if(traffic_status[red]):
        red_led.on()
    else:
        red_led.off()
        
def main():
    traffic_light = {'red_LED':0, 'yellow_LED' :1, 'green_LED' :1}
    stop_light(traffic_light)                                                                                                                                                                                                                                                                                                                                                                     
    
main()