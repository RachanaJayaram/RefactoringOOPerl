str_=lambda x: '' if x==None else str(x)
x=None
y=None
z=None
end_=''
sep_=''


def foo (end_ , sep_ , x , y , z , *argv) : 
	arg_list=list(argv)[::-1]
	z =  arg_list.pop()
	my_y = 20
	local_z = 30
	print( "foo before g : \n x : " + str_(x) + " y : " + str_(my_y) + " z : " + str_(local_z) + " \n",end=end_,sep=sep_ )
	# x: 10 y: 20 z: 30 
	(end_ , sep_ , x , y , local_z)=g(  end_ , sep_ , x , y , local_z )
	print( "foo after g : \n x : " + str_(x) + " y : " + str_(my_y) + " z : " + str_(local_z) + " \n",end=end_,sep=sep_ )
	#x: 2 y: 20 z: 3
	print( "foo global : \n y : ",y,"\n",end=end_,sep=sep_ )
	# y : 2
	return( end_,sep_,x,y,z )

def g (end_ , sep_ , x , y , z , *argv) : 
	arg_list=list(argv)[::-1]
	print( "g : \n x : " + str_(x) + " y : " + str_(y) + " z : " + str_(z) + " \n",end=end_,sep=sep_ )
	# x: 10 y :  z: 30
	x = 2
	y = 2
	z = 3
	return( end_,sep_,x,y,z )
x = 10
print( "main before foo : \n x : " + str_(x) + " y : " + str_(y) + " z : " + str_(z) + " \n",end=end_,sep=sep_ )
# x: 10 y:  z:  
(end_ , sep_ , x , y , z)=foo(  end_ , sep_ , x , y , z , x )
print( "main after foo : \n x : " + str_(x) + " y : " + str_(y) + " z : " + str_(z) + " \n",end=end_,sep=sep_ )
# x : 2 y:2 z :10

def scope_test (end_ , sep_ , *argv) : 
	arg_list=list(argv)[::-1]
	local_sep_ = ""
	local_end_ = ""
	print( "to","get","her",end=local_end_,sep=local_sep_ )
	print( "to","get","her",end=local_end_,sep=local_sep_ )
	return( end_,sep_ )
sep_ = "\t"
# output field sep
end_ = "\t"
# output field sep
print( "hello","world",end=end_,sep=sep_ )
print( "hello","world",end=end_,sep=sep_ )
(end_ , sep_)=scope_test(  end_ , sep_ )
print( "hello","world",end=end_,sep=sep_ )
