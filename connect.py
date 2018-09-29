from kulka import Kulka
import time

sphero = Kulka('68:86:E7:09:23:79')

count = 0

while (count < 5):
	sphero.set_rgb(0xFF, 0, 0)
	sphero.roll(35,0)
	time.sleep(10)	
	sphero.roll(35,180)
	time.sleep(10)
	count += 1
