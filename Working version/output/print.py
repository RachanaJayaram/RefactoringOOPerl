from parent import parent
from grandparent import grandparent

class child( parent,grandparent ) :
	def hi(self,*argv):
		arg_list=list(argv)[::-1]
		name = "skanda"
		print( "hello" + name , end = '' )
