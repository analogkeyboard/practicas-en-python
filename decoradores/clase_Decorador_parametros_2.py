def decorador_args(arg1,arg2,arg3):

	def wrap(f):

		print("inicio wrap:()")

		def wrapped_f(*args):

			print("inicio wraped_f")

			print("decorator args:",arg1,arg2,arg3)

			f(*args)

			print("fin wraped_f")

		return wrapped_f

	return wrap


@decorador_args(1,2,3)
def funcion(a,b):
	print("funcion args:",a,b)

funcion("p1", "p2")