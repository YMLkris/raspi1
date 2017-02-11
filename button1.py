from gpiozero import Button, LED
from time import sleep

button=Button(12)
led = LED(17)

while True:
    button.wait_for_press()
    print("Hey, stop pressing me!")
    led.on()
    sleep(3)
    led.off()
    
    
