from mcpi.minecraft import Minecraft
import time
#from mcpi import block
#from minecraftstuff import MinecraftDrawing
#https://minecraft-stuff.readthedocs.io/en/latest/minecraftdrawing.html
#https://github.com/martinohanlon/minecraft-stuff
# https://github.com/martinohanlon/mcpi
mc = Minecraft.create("minecraft-server")
mc.postToChat("Hello World!")
mc.player.setTilePos(2, 2, 1)
melon = 100
lana = 35
hola = 125
sign = 68
#https://minecraft-ids.grahamedgecombe.com/
for y in range(50):
  time.sleep(0.5)
  z = y + 1
  mc.setBlock(10, y, z,lana)
  mc.setSign(10, y, z,sign, 2)
