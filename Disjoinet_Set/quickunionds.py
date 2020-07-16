class QuickUion(object):
	"""docstring for QuickUion"""
	def __init__(self, n):
		self.sets = [i for i in range(n)]

	def connect(self, a, e):
		a_id = self.sets[a]
		e_id = self.sets[e]
		self.sets[e] = a_id

	def find_root(self, i):
		if i != self.sets[i]:
			i = self.sets[i]
		return i


	def is_connect(self, c, d):
		return self.find_root(c) == self.find_root(d)


def get_connect(n):
	for _ in range(n):
		a,b = input().split(' ')
		a = int(a)
		b = int(b)
		question.connect(a, b)

def check_connect(n):
	for _ in range(n):
		a,b = input().split(' ')
		a = int(a)
		b = int(b)
		print(question.is_connect(a, b))
if __name__ == '__main__':
	a = int(input())
	question = QuickUion(a)
	b = int(input())
	get_connect(b)
	c = int(input())
	check_connect(c)






		


		