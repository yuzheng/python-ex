#-*-coding:UTF-8 -*-
# 範例程式 EX02_05.py
#
# 輸入一個數字n，計算1+2+3+...+n的總和為多少?
# (for 迴圈版本)

n = int(input('Please input n:'))
total = 0

#range(a,b) 產生a 到 b-1的數字,例如range(1,5)=>1,2,3,4
for i in range(1,n+1):
    # total += i  等價於 total = total + i
    total += i
print('Total is:',total)

# (while 迴圈版本)

#n = int(input('Please input n:'))
total = 0
i = 1

while i <= n:
    # total += i  等價於 total = total + i
    total += i
    i += 1
print('Total is:',total)