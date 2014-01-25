#generates a bot

import os
import random

botNumber = 12345

temp  = open('randomTemplate.gen', 'r')
output = open('./bots/bot'+str(botNumber)+'.py', 'w')
clean  = temp.read().replace("###", str(random.randint(0,100)*.01))
output.write(clean)
output.close()
