class QuickUnionDS(object):
	def __init__(self, N):
		self.__id = list(range(0, N))

	def __get_root(self, p):
		pid = self.__id[p]
		while pid != self.__id[pid]:
			pid = self.__id[pid]

		return pid

	def is_connected(self, p, q):
		return self.__get_root(p) == self.__get_root(q)

	def connect(self, p, q):
		p_root = self.__get_root(p)
		q_root = self.__get_root(q)

		self.__id[p_root] = self.__id[q_root]

N = int(input())
ds = QuickUnionDS(N)
n = int(input())
for _ in range(n):
	s = input()
	a, b = s.split(' ')
	a = int(a)
	b = int(b)
	ds.connect(a, b)
m = int(input())
for _ in range(m):
	s = input()
	a, b = s.split(' ')
	a = int(a)
	b = int(b)
	print(ds.is_connected(a, b))