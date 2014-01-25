#generates a student bot

import os
import sys
import inspect

id = raw_input('Please enter your student ID number: ')

print 'Student ID: ',id

student = open('studentCode'+id+'.txt')

temp  = open('../../studentTemplate.gen', 'r')
output = open('../../bots/student'+str(id)+'.py', 'w')

newcode  = temp.read().replace('###',id) + '\n' + student.read()

output.write(newcode)
output.close()

temp.close()

student.close()
sys.exit()