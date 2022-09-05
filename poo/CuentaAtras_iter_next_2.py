class CuentaAtras(object):
	"""docstring for CuentaAtras"""
	def __init__(self, low,high):
		self.current = low
		self.high = high

	def __iter__(self):
		return self

	def __next__(self):
		if self.current >self.high:
			raise StopIteration

		# r=self.count
		self.current=self.current+1
		return self.current-1

for x in CuentaAtras(5,9):
	print(x)