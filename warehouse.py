import mcpi.minecraft as minecraft
mc = minecraft.Minecraft.create()

block=20
air = 9

pos = mc.player.getPos()
x = pos.x + 5
y = pos.y 
z = pos.z + 5

x2= x + 10
y2 = y + 5
z2 = z + 8

mc.setBlocks(x, y, z, x2, y2, z2, block)

mc.setBlocks(x + 1, y + 1, z + 1, x2 -1, y2, z2 - 1, air)



