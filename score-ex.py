#!/usr/bin/python
#http://www.tutorialspoint.com/python/python_command_line_arguments.htm
#ex: python3 score.py AAA:80,82,73,69 BBB:90,88,67,73 CCC:77,92,82,70

import sys

#print('Number of arguments:', len(sys.argv), 'arguments.')
#print('Argument List:', str(sys.argv))

#students = sys.argv
students = {"Tom":[100,90,88,95,55], "John":[70,78,60,89], "Amy":[50,66,20,88,30], "Bob":[99,64,80,72,90], "Tony":[100,83,92] }
#print(students)
#print(type(students))
#students.pop(0)

#max
firstStudent = {"name":"","score":0}
#min
lastStudent = {"name":"","score":9999}

for student,scores in students.items():
	sum = 0
	index = 0
	for score in scores:
		sum += float(score)
		index = index + 1
	avg = sum/index
	if avg > firstStudent["score"]:
		firstStudent["name"] = student
		firstStudent["score"] = avg
	if avg < lastStudent["score"]:
		lastStudent["name"] = student
		lastStudent["score"] = avg
	print(student,': sum is ',sum, ' and avg is ',avg)
print('The highest student:',firstStudent["name"],': avg is ',firstStudent["score"])
print('The lowest student:',lastStudent["name"],': avg is ',lastStudent["score"])
