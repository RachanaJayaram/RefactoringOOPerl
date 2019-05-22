str_=lambda x: '' if x==None else str(x)
class date :
	
	def __init__(self,*argv) : 
		arg_list=list(argv)[::-1]
		self.__dict__.update({'dd':arg_list.pop(),'mm':arg_list.pop(),'yy':arg_list.pop()})
	
	def dispdate (self,end_ , sep_ , *argv) : 
		arg_list=list(argv)[::-1]
		print( self.dd,"//",self.mm,"//",self.yy,'=',self.dd + self.mm + self.yy,end=end_,sep=sep_ )
		print( self.dd,"//",self.mm,"//",self.yy,'=',self.dd + self.mm - self.yy,end=end_,sep=sep_ )
		print( self.dd,"//",self.mm,"//",self.yy,'=',self.dd + self.mm * self.yy,end=end_,sep=sep_ )
		print( self.dd,"//",self.mm,"//",self.yy,'=',self.dd + self.mm / self.yy,end=end_,sep=sep_ )
		return( end_,sep_ )
	
	def dispdate2 (self,end_ , sep_ , *argv) : 
		arg_list=list(argv)[::-1]
		print( self.dd,"//",self.mm,"//",self.yy,'=',self.dd + self.mm / self.yy,end=end_,sep=sep_ )
		print( self.dd,"//",self.mm,"//",self.yy,'=',self.dd + self.mm * self.yy,end=end_,sep=sep_ )
		return( end_,sep_ )
