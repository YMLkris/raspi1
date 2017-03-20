import mcpi.minecraft as minecraft # Import the Minecraft Python Library
mc = minecraft.Minecraft.create() # Create an instance inside Minecraft called mc

import time # Import time library

while True:
    pos = mc.player.getPos() #Vec3 3d vector class, so "pos" has an x,y,and z float
    x = pos.x
    y = pos.y
    z = pos.z - 1

    block = 38 #block 38 = cyan flower

    mc.setBlock(x, y, z, block) # put it all together to set a flower next to you

    time.sleep(0.2)

    
#Challenges:
    # make flowers change color from blue to yellow
    # create tower of blocks next to you so you can build walls
