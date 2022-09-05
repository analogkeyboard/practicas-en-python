class TestBool(object):
	def __bool__(self):
		return False

t=TestBool()
t.__bool__()

print(bool(t))

if t:
	print("Es falso")