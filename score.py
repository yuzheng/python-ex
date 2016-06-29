#!/usr/bin/python
#http://www.tutorialspoint.com/python/python_command_line_arguments.htm
#ex: python3 score.py AAA:80,82,73,69 BBB:90,88,67,73 CCC:77,92,82,70

import sys

print('Number of arguments:', len(sys.argv), 'arguments.')
print('Argument List:', str(sys.argv))

students = sys.argv
#print(students)
#print(type(students))
students.pop(0)

#max
firstStudent = {"name":"","score":0}
#min
lastStudent = {"name":"","score":9999}

for student in students:
	sum = 0
	index = 0
	info = student.split(':')
	scores = info[1].split(',')
	for score in scores:
		sum += float(score)
		index = index + 1
	avg = sum/index
	if avg > firstStudent["score"]:
		firstStudent["name"] = info[0]
		firstStudent["score"] = avg
	if avg < lastStudent["score"]:
		lastStudent["name"] = info[0]
		lastStudent["score"] = avg
	print(info[0],': sum is ',sum, ' and avg is ',avg)
print('first student:',firstStudent["name"],': avg is ',firstStudent["score"])
print('last student:',lastStudent["name"],': avg is ',lastStudent["score"])
