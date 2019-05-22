str_=lambda x: '' if x==None else str(x)
a=None
b=None
c=None
n=None
area=None
perimeter=None
x=None
y=None
end_=''
sep_=''
import sys
sys.path.insert(0, 'G:\\extra\\oo_perl\\Rachana_Version\\version4\\testing\\input\\')
import server.rect as rect


def fibonacci (a , b , c , end_ , n , sep_ , *argv) : 
	arg_list=list(argv)[::-1]
	local_sep_ = ".\t"
	n =  arg_list.pop()
	print( str_(n) + " terms of the fibonacci series\n",end=end_,sep=local_sep_ )
	local_end_ = ".\t"
	a = 0
	b = 1
	print( str_(a) + " ",str_(b) + " ",end=local_end_,sep=local_sep_ )
	for i in range (2,n+1,1):
			c = a + b
			print( str_(c) + " ",end=local_end_,sep=local_sep_ )
			a = b
			b = c
	return( a,b,c,end_,n,sep_ )
x = 2
y = 3
print( "Constructing a rectangle of length " + str_(x) + " and breadth " + str_(y) + " \n",end=end_,sep=sep_ )
#Constructing a rectangle of length $x and breadth $y 
d=rect.rect(x,y)
#area and perimeter 
area = d.area()
perimeter = d.perimeter()
print( "A rectangle of length " + str_(x) + " and breadth " + str_(y) + " \nHas area = " + str_(area) + " \t perimeter = " + str_(perimeter) + " \n",end=end_,sep=sep_ )
sep_ = " "
end_ = "\n"
print( "Fibonacci",end=end_,sep=sep_ )
(a , b , c , end_ , n , sep_)=fibonacci(  a , b , c , end_ , n , sep_ , area )
