class DataIndexIntegerSet(object):
	"""docstring for DataIndexIntegerSet"""
	def __init__(self):
		self.__present = [False]*16

	def add(self, x):
		self.__present[x] = True

	def contains(self, x):
		return self.__present[x]
strs = ['abc','bac','cab']
for word in strs:
	sorted_word = ''.join(sorted(word))
	print(sorted_word)