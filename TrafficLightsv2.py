from gpiozero import LED
import time

# Define LED pins (Using Raspberry Pi GPIO numbering)
red_led = LED(17)      # GPIO Pin 17, pin number 11
yellow_led = LED(27)   # GPIO Pin 27, pin number 13
green_led = LED(22)    # GPIO Pin 22, pin number 15

def stop_light(traffic_status):
    """Controls the LEDs based on user input"""
    if traffic_status['red_LED']:
        red_led.on()
    else:
        red_led.off()
        
    if traffic_status['yellow_LED']:
        yellow_led.on()
    else:
        yellow_led.off()
        
    if traffic_status['green_LED']:
        green_led.on()
    else:
        green_led.off()

def main():
    print("Traffic Light Control - Enter 0 (OFF) or 1 (ON) for each light.")
    
    while True:
        try:
            red_input = int(input("Enter 1 to turn on Red LED, 0 to turn off: "))
            yellow_input = int(input("Enter 1 to turn on Yellow LED, 0 to turn off: "))
            green_input = int(input("Enter 1 to turn on Green LED, 0 to turn off: "))

            if red_input not in [0, 1] or yellow_input not in [0, 1] or green_input not in [0, 1]:
                print("Invalid input! Please enter 0 or 1.")
                continue
            
            traffic_light = {'red_LED': red_input, 'yellow_LED': yellow_input, 'green_LED': green_input}
            stop_light(traffic_light)

        except ValueError:
            print("Invalid input! Please enter a number (0 or 1).")

main()