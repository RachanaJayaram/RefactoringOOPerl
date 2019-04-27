# !/usr/local/bin/perl -w -I G:\extra\oo_perl\Rachana_Version\version4\testing\input\
import sys
sys.path.insert(0, 'G:\\extra\\oo_perl\\Rachana_Version\\version4\\testing\\input\\')
import server.rect as rect
x=10
y=15
print("Constructing a rectangle of length "+str(x)+" and breadth "+str(y)+" \n",end='',sep='')
#Constructing a rectangle of length $x and breadth $y 
d=rect.rect(x,y)
d.area()
#area and perimeter 
area=d.area()
perimeter=d.perimeter()
print("A rectangle of length "+str(x)+" and breadth "+str(y)+" \nHas area = "+str(area)+" \t perimeter = "+str(perimeter)+" \n",end='',sep='')
