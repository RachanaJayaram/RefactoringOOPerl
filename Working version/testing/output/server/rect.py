class rect :
	
	def __init__(self,*argv) : 
		arg_list=list(argv)[::-1]
		self.__dict__.update({'length':arg_list.pop(),'breadth':arg_list.pop()})
	
	def area (self,*argv) : 
		arg_list=list(argv)[::-1]
		return(self.length * self.breadth)
	
	def perimeter (self,*argv) : 
		arg_list=list(argv)[::-1]
		return(self.length * 2 + self.breadth * 2)
