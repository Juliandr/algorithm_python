class Point(object):
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def __sub__(self, other):
		return Point(self.x - other.x, self.y - other.y)

	def __add__(self, other):
		return Point(self.x + other.x, self.y + other.y)

	def __eq__(self, other):
		return self.x == other.x and self.y == other.y

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

	def get(self, p):
		return self.__map[p.y][p.x]

	def set(self, p, v):
		self.__map[p.y][p.x] = v

	def __str__(self):
		s = ''
		for line in self.__map:
			line = [str(i) for i in line]
			s += ' '.join(line) + '\n'
		return s


class BreadFirstPaths(object):
	def __init__(self, m, s, t):
		self.map = m
		self.s = s
		self.t = t
		# 可走的四个方向集合
		self.d = [Point(1, 0), Point(-1, 0), Point(0, 1), Point(0, -1)]
		self.from_v = Map(self.map.n, self.map.m, None)
		self.marked = Map(self.map.n, self.map.m, False)
		self.marked.set(self.s, True)
		self.min_corners = Map(self.map.n, self.map.m, float('inf'))
		self.min_corners.set(self.s, 0)
		self.directions = Map(self.map.n, self.map.m, None)
		self.bfs(s, t)

	def bfs(self, s, t):
		self.fringe = []
		self.fringe.append(s)
		result_found = False
		while self.fringe and not result_found:
			# print([str(i) for i in self.fringe])
			v = self.fringe.pop(0)
			for d in self.d:
				if self.try_goto(v, d):
					result_found = True
					break

	def reachable(self, v):
		# 判断w是否超过地图边界
		if not (v.x>=0 and v.x<self.map.m and v.y>=0 and v.y<self.map.n):
			return False

		# 判断v点是不是墙
		if self.map.get(v) == '1':
			return False

		return True

	def try_goto(self, v, d):
		# try_goto(w, v): 尝试从节点v往d方向一直走下去

		# 这里v和d都是Point类实例，我们在Point里定义了__add__等函数
		# 使得我们可以直接对两个实例进行相加、相减、判断相等等操作
		# 得到的结果也是一个Point类的实例
		next_point = v + d

		# 横向为1，纵向为0
		# d.x为1说明在x方向上移动，即横向
		direction = abs(d.x)
		
		# 看一下到达当前v节点已经拐了几次弯
		corners = self.min_corners.get(v)
		if self.directions.get(v) is not None:
			# 如果方向不一样则说明拐弯了
			if direction != self.directions.get(v):
				corners += 1
		else:
			corners = 0

		# 只要这个方向可以一直走下去那就不断循环
		while self.reachable(next_point):
			if corners < self.min_corners.get(next_point):
				if not self.marked.get(next_point):
					self.fringe.append(next_point)
					self.marked.set(next_point, True)
				self.from_v.set(next_point, v)
				self.directions.set(next_point, direction)
				self.min_corners.set(next_point, corners)

			if next_point == self.t:
				return True

			next_point = next_point + d

		return False

	def get_min_corners(self):
		return self.min_corners.get(self.t)

	def get_path(self):
		print(self.s.x, self.s.y)
		path = []
		p = self.t
		while p.x != self.s.x or p.y != self.s.y:
			path.insert(0, (p.x+1, p.y+1))
			p = self.from_v.get(p)
		path.insert(0, (p.x+1, p.y+1))
		return path


n, m = input().split(' ')
n = int(n)
m = int(m)
map_list = []
for _ in range(n):
	s_input = input()
	s_list = s_input.split(' ')
	map_list.append(s_list)

x1, y1, x2, y2 = input().split(' ')
x1 = int(x1) - 1
x2 = int(x2) - 1
y1 = int(y1) - 1
y2 = int(y2) - 1

bfp = BreadFirstPaths(Map(n, m, None, map_list), Point(x1, y1), Point(x2, y2))
print(bfp.get_min_corners())
print(bfp.get_path())