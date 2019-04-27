print("12 terms of the fibonacci series\n",end='',sep='')
a=0
b=1
print(str(a)+" "+str(b)+" ",end='',sep='')
for i in range (2,13,1):
		c=a + b
		print(str(c)+" ",end='',sep='')
		a=b
		b=c
print("\n",end='',sep='')
