str_=lambda x: '' if x==None else str(x)
area=None
perimeter=None
x=None
y=None
# !/usr/local/bin/perl -w -I G:\extra\oo_perl\Rachana_Version\version4\testing\input\
import sys
sys.path.insert(0, 'G:\\extra\\oo_perl\\Rachana_Version\\version4\\testing\\input\\')
import server.rect as rect
x = 10
y = 15
print( "Constructing a rectangle of length " + str_(x) + " and breadth " + str_(y) + " \n",end='',sep='' )
#Constructing a rectangle of length $x and breadth $y 
d=rect.rect(x,y)
d.area()
#area and perimeter 
area = d.area()
perimeter = d.perimeter()
print( "A rectangle of length " + str_(x) + " and breadth " + str_(y) + " \nHas area = " + str_(area) + " \t perimeter = " + str_(perimeter) + " \n",end='',sep='' )
