#generates a number of bots

import os
import sys
import random

number = 10

x =  000001
while (x <= number):
	botNumber = x
	temp  = open('randomTemplate.gen', 'r')
	output = open('./bots/bot'+str(botNumber).zfill(6)+'.py', 'w')
	clean  = temp.read().replace("###", str(random.randint(0,100)*.01))
	output.write(clean)
	output.close()
	x += 1
sys.exit()