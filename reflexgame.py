from gpiozero import LED, Button
from time import sleep
from random import uniform

led = LED(24)
right_button = Button(16)
left_button = Button(12)

round = 1
right_score = 0
left_score = 0
pressed = False

left_name = input('left player enter your name:')
right_name = input('right player enter your name:')

while(round < 12):

    print('Round ' + str(round))

    led.on()
    sleep(uniform(2, 4))
    led.off()

    while(pressed == False):
        if(right_button.is_pressed):
            right_score+=1
            print(right_name + ' won the round!')
            pressed = True
        
        if(left_button.is_pressed):
            left_score+=1
            print(left_name + ' won the round!')
            pressed = True

    pressed = False
    global round
    round += 1
print('**********************************')
print('*****  Game Over! *****')
print(right_name +': ' + str(right_score) + '   ' + left_name + ': ' + str(left_score))
if (right_score > left_score):
    print(right_name + ' wins!')
else:
    print(left_name + ' wins!')
    
