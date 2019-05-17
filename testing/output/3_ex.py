str_=lambda x: '' if x==None else str(x)
x=None
y=None
z=None


def foo (x , y , z , *argv) : 
	arg_list=list(argv)[::-1]
	z =  arg_list.pop()
	my_y = 20
	local_z = 30
	print( "foo before g : \n x : " + str_(x) + " y : " + str_(my_y) + " z : " + str_(local_z) + " \n",end='',sep='' )
	# x: 10 y: 20 z: 30 
	(x , y , local_z)=g(  x , y , local_z )
	print( "foo after g : \n x : " + str_(x) + " y : " + str_(my_y) + " z : " + str_(local_z) + " \n",end='',sep='' )
	#x: 2 y: 20 z: 3
	print( "foo global : \n y : ",y,"\n",end='',sep='' )
	# y : 2
	return( x,y,z )

def g (x , y , z , *argv) : 
	arg_list=list(argv)[::-1]
	print( "g : \n x : " + str_(x) + " y : " + str_(y) + " z : " + str_(z) + " \n",end='',sep='' )
	# x: 10 y :  z: 30
	x = 2
	y = 2
	z = 3
	return( x,y,z )
x = 10
print( "main before foo : \n x : " + str_(x) + " y : " + str_(y) + " z : " + str_(z) + " \n",end='',sep='' )
# x: 10 y:  z:  
(x , y , z)=foo(  x , y , z , x )
print( "main after foo : \n x : " + str_(x) + " y : " + str_(y) + " z : " + str_(z) + " \n",end='',sep='' )
# x : 2 y:2 z :10
