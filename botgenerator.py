#generates a bot

import os
import random

botNumber = 12345

temp  = open('randomTemplate.py', 'r')
output = open('./bots/bot'+str(botNumber), 'w')
clean  = temp.read().replace("###", str(random.randint(0,100)*.01))
output.write(clean)