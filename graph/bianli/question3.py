class Point(object):
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def __str__(self):
		return '({} {})'.format(self.x, self.y)


class Map(object):
	def __init__(self, n, m, default=None, map=None):
		self.m = m
		self.n = n
		if map is None:
			self.__map = [[default for _ in range(m)] for _ in range(n)]
		else:
			self.__map = list(map)

	def get(self, x, y):
		return self.__map[y-1][x-1]

	def set(self, x, y, v):
		self.__map[y-1][x-1] = v

	def __str__(self):
		s = ''
		for line in self.__map:
			line = [str(i) for i in line]
			s += ' '.join(line) + '\n'
		return s


class BreadFirstPaths(object):
	def __init__(self, m, s, t, mp):
		self.map = m
		self.s = s
		self.t = t
		self.mp = mp
		self.from_v = Map(self.map.n, self.map.m, None)
		self.min_mps = Map(self.map.n, self.map.m, None)
		self.bfs(s, t)

	def bfs(self, s, t):
		self.fringe = []
		self.fringe.append(s)
		self.min_mps.set(s.x, s.y, 0)
		while self.fringe:
			# print([str(i) for i in self.fringe])
			v = self.fringe.pop(0)
			if v.x > 1:
				w = Point(v.x - 1, v.y)
				self.try_goto(w, v)
			if v.x < self.map.m:
				w = Point(v.x + 1, v.y)
				self.try_goto(w, v)
			if v.y > 1:
				w = Point(v.x, v.y - 1)
				self.try_goto(w, v)
			if v.y < self.map.n:
				w = Point(v.x, v.y + 1)
				self.try_goto(w, v)
			if v.x*2 <= self.map.m and v.y*2 <= self.map.n:
				w = Point(v.x * 2, v.y * 2)
				self.try_goto(w, v)

	def try_goto(self, w, v):
		# try_goto(w, v): 尝试从节点v到节点w

		# 如果要去的w点是墙则直接返回
		if self.map.get(w.x, w.y) == '1':
			return

		# 如果我们是从w到v节点的那么没必要走回头路了
		v_from = self.from_v.get(v.x, v.y)
		if v_from is not None:
			if v_from.x == w.x and v_from.y == w.y:
				return

		mp = self.min_mps.get(v.x, v.y) + 1
		# 超过体力值了直接返回，此路不通
		if mp > self.mp:
			return

		if self.min_mps.get(w.x, w.y) is not None:
			# 如果之前走过w点且当前这条路的拐弯次数更少则更新数据
			if mp < self.min_mps.get(w.x, w.y):
				self.fringe.append(w)
				self.from_v.set(w.x, w.y, v)
				self.min_mps.set(w.x, w.y, mp)
		else:
			self.fringe.append(w)
			self.from_v.set(w.x, w.y, v)
			self.min_mps.set(w.x, w.y, mp)

	def count_mp(self):
		return self.min_mps.get(self.t.x, self.t.y)

mp = int(input())
n, m = input().split(' ')
n = int(n)
m = int(m)
map_list = []
for _ in range(n):
	s_input = input()
	s_list = s_input.split(' ')
	map_list.append(s_list)

x1, y1, x2, y2 = input().split(' ')
x1 = int(x1)
x2 = int(x2)
y1 = int(y1)
y2 = int(y2)

bfp = BreadFirstPaths(Map(n, m, None, map_list), Point(x1, y1), Point(x2, y2), mp)
# print(bfp.from_v)
print(bfp.count_mp())