def principal(f):
	def nueva():
		print("inicio:",f.__name__)
		f()
		print("fin:",f.__name__)
	return nueva

@principal
def decorada():
	print("decorada")

decorada()