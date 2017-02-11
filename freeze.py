import mcpi.minecraft as minecraft
mc = minecraft.Minecraft.create ()

import time

while True:
    time.sleep(0.2)
    pos = mc.player.getPos()
    x = pos.x
    y = pos.y
    z = pos.z

    blockBelow = mc.getBlock(x, y - 1, z)

    wood = 9
    ice = 79

    if blockBelow == water or ice:
        mc.setBlock(x, y - 1, z, ice)
        mc.setBlock(x + 1, y - 1, z, ice)
        mc.setBlock(x - 1, y - 1, z, ice)
        mc.setBlock(x, y - 1, z + 1, ice)
        mc.setBlock(x, y - 1, z - 1, ice)
