class Test(object):
	def __init__(self):
		self.x=3
		self.y=4
		self.z=5

attrs={"x":1,"y":2,"z":3}

t=Test()

for k,v in attrs.items():
	t.__setattr__(k, v)

for k in attrs.keys():
	print("{0}={1}".format(k,t.__getattribute__(k)))