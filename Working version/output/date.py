class date:
	
	def __init__(self,*argv) : 
		arg_list = list(argv)[::-1]
		self.__dict__.update({'dd':arg_list.pop(),'mm':arg_list.pop(),'yy':arg_list.pop()})
	
	def dispdate(self,*argv):
		arg_list=list(argv)[::-1]
		self.self=arg_list.pop()
		print(self.dd,"//",self.mm,"//",self.yy,'=',self.dd + self.mm + self.yy,end='')
		print(self.dd,"//",self.mm,"//",self.yy,'=',self.dd + self.mm - self.yy,end='')
		print(self.dd,"//",self.mm,"//",self.yy,'=',self.dd + self.mm * self.yy,end='')
		print(self.dd,"//",self.mm,"//",self.yy,'=',self.dd + self.mm / self.yy,end='')
	
	def dispdate2(self,*argv):
		arg_list=list(argv)[::-1]
		print(self.dd,"//",self.mm,"//",self.yy,'=',self.dd + self.mm / self.yy,end='')
		print(self.dd,"//",self.mm,"//",self.yy,'=',self.dd + self.mm * self.yy,end='')
