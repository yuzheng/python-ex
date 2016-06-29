#-*-coding:UTF-8 -*-
#
# 判斷輸入是否為整數(int)

input_string = input('Please input n:')
#while input_string.isdigit() == False:
while not input_string.isdigit():
	print("Error, %s is not digit!" % input_string)
	input_string = input('Please input n:')	
print("%s is digit!" % input_string)
