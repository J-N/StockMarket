#generates a student bot

import os
import sys
import inspect

id = raw_input('Please enter your student ID number: ')

print 'Student ID: ',id

student = open('studentCode'+id+'.txt')

temp  = open('../studentTemplate.gen', 'r')
output = open('../bots/student'+str(id)+'.py', 'w')

clean  = temp.read().replace("#studentCode#",student.read)
output.write(clean)
output.close()
temp.close()
student.close()
sys.exit()