from gpiozero import LED
from gpiozero import PWMLED
from gpiozero import Servo
from time import sleep

r_red_pwm_pin = PWMLED(14)
r_green_pwm_pin = PWMLED(15)
r_blue_pwm_pin = PWMLED(18)

l_red_pwm_pin = PWMLED(27)
l_green_pwm_pin = PWMLED(22)
l_blue_pwm_pin = PWMLED(23)

def eyes_RGB(eyes):
    if debug_messages : print("Running eyes_RGB function")
    if debug_messages : print(eyes)
       
    left_eye, right_eye = eyes
    if debug_messages : print(left_eye)
    if debug_messages : print(right_eye)
    
def get_robot_feature_data():
    hex_code = "#4ebd51"
    hex_code = hex_code.upper()
    print(hex_code)
    hex_green = hex_code[3:5]
    print(hex_green)
    dec_hex_green = int(hex_green,16)
    print(dec_hex_green)
    green_brightness = dec_hex_green / 256
    print(green_brightness)
    if debug_messages : print("Runninng get_robot_feature_data function")
    right_eye = {'leye_red_RGBLED':.44, 'leye_green_RGBLED':green_brightness, 'leye_blue_RGBLED':.99}
    left_eye =  {'reye_red_RGBLED':1, 'reye_green_RGBLED':green_brightness, 'reye_blue_RGBLED':.99}
    stop_light = {'red_LED':1, 'yellow_LED':0, 'green_LED':0}
    # servo
    rfd = [stop_light, left_eye, right_eye]
    if debug_messages : print(rfd)
    if debug_messages : print("Returning get_robot_feature_data function")
    return(rfd)

def main():
    print("Welcome To The STEAM Clown Makey Bot")
    if debug_messages : print("Calling get_robot_feature_data function")
#    robot_features = get_robot_feature_data()
    stop_light_LEDs, left_RGB, right_RGB = get_robot_feature_data()
    if debug_messages : print(stop_light_LEDs)
    if debug_messages : print(left_RGB)
    if debug_messages : print(right_RGB)

    if debug_messages : print("Calling stop_light function")
    stop_light(stop_light_LEDs)
    if debug_messages : print("Returned from stop_light function")

    if debug_messages : print("Calling eyes_RGB function")
    eyes_RGB([left_RGB,right_RGB])
    if debug_messages : print("Returned from eyes_RGB function")
    wave("im going to send data later")
    
main()