
def funA(x):
	"""
	These are comments about funA
	output = 2 times input
	"""
	a = 2*x
	return a


def funB(x):
	"""
	These are comments about funB
	output = 4 plus input
	"""
	a = 4 + x
	return a
	

def my_fun(x):
	"""
	clip to 1
	"""
	if x > 1:
		return 1.0
	elif x < -1:
		return -1.0
	else:
		return x
