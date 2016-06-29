#-*-coding:UTF-8 -*-
#
# 分別用for，while迴圈各寫⼀個nxn的乘法表 
# 程式可以讀取使用者輸入的值 n, n>1 
# 輸出範例: ex. n=3 1*1 = 1 1*2 = 2 1*3 = 3 2*1 = 2 2*2 = 4 2*3 = 6 3*1 = 3 3*2 = 6 3*3 = 9
# (for 迴圈版本)

n = int(input('Please input n:'))
print("for version")
#range(a,b) 產生a 到 b-1的數字,例如range(1,5)=>1,2,3,4
for i in range(1,n+1):
	for j in range(1,n+1):
		#print(" %d * %d = %d" % (i,j,i*j))
		print(" %(a)d * %(b)d = %(c)d" % {'a':i,'b':j,'c':i*j})
# (while 迴圈版本)
#n = int(input('Please input n:'))
print("while version")
p = 1
while p <= n:
	q = 1
	while q <= n:
		#print(p,"*",q," = ",p*q)
		#print(" {0} * {1} = {2} ".format(p,q,p*q))
		#print(" {} * {} = {} ".format(p,q,p*q))
		print(" {a} * {b} = {c} ".format(b=p,a=q,c=p*q))
		q += 1
	p += 1
