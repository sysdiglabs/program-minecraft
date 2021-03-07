from mcpi.minecraft import Minecraft
import time
#from mcpi import block
#from minecraftstuff import MinecraftDrawing
#https://minecraft-stuff.readthedocs.io/en/latest/minecraftdrawing.html
#https://github.com/martinohanlon/minecraft-stuff
# https://github.com/martinohanlon/mcpi
mc = Minecraft.create("minecraft-server")

mc.postToChat("Hello World!")
#mc.player.setTilePos(2, 0, 0)
melon = 100
#https://minecraft-ids.grahamedgecombe.com/
for x in range(100):
  time.sleep(0.5)
  y = x+1
  mc.setBlock(10, x, y, melon)
