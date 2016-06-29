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
firstStudent = {}
#min
lastStudent = {}

maxcount = 0

for student,scores in students.items():
	count = 0
	for score in scores:
		count = count + 1
	if maxcount < count:
		maxcount = count
print("maxcount:%d"%maxcount)
for student,scores in students.items():
	sum = 0
	count = 0
	for score in scores:
		sum += float(score)
		count = count + 1
	studentDict = {"name":student,"sum":sum,"count":count,"avg":sum/count}
	#studentDict = {"name":student,"sum":sum,"count":count,"avg":sum/maxcount}
	if not firstStudent:
		firstStudent = studentDict
	if not lastStudent:
		lastStudent = studentDict
	if studentDict["avg"] > firstStudent["avg"]:
		firstStudent = studentDict
	if studentDict["avg"] < lastStudent["avg"]:
		lastStudent = studentDict	
	print(studentDict)
print('The highest student:',firstStudent["name"],': avg is ',firstStudent["avg"])
print('The lowest student:',lastStudent["name"],': avg is ',lastStudent["avg"])
