class mod:
	def add(*argv):
		arg = (list(argv)[1:]).reverse()
		a=arg.pop()
		b=arg.pop()
		c=a+b
		return c
