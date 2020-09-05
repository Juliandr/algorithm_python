class DFS(object):
	def __init__(self, n, available_pos, m):
		self.ap = available_pos
		self.n = n
		self.m = m
		self.rows = [False for _ in range(self.n)]
		self.cols = [False for _ in range(self.n)]
		self.count = self.dfs(len(self.ap) - 1, m)
	
	def dfs(self, index, chesses_left):
		x, y = self.ap[index]
		if chesses_left == 0:
			return 1
		elif index == 0:
			if not self.rows[y] and not self.cols[x] and chesses_left == 1:
				return 1
			else:
				return 0
		else:
			if not self.rows[y] and not self.cols[x]:
				self.rows[y] = True
				self.cols[x] = True
				counts = self.dfs(index - 1, chesses_left - 1)
				self.rows[y] = False
				self.cols[x] = False
				counts += self.dfs(index - 1, chesses_left)
				return counts
			else:
				counts = self.dfs(index - 1, chesses_left)
				return counts

s = input()
n, m = s.split(' ')
n = int(n)
m = int(m)
map_list = [[] for _ in range(n)]
available_pos = []
for i in range(n):
	s_input = input()
	for j, s in enumerate(s_input):
		map_list[i].append(s)
		if s == '#':
			available_pos.append((j, i))

dfs = DFS(len(map_list), available_pos, m)
print(dfs.count)