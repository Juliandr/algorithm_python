class DFS(object):
	def __init__(self, map_list, m):
		self.map = map_list
		self.n = len(self.map)
		self.m = m
		self.cols = [False for _ in range(self.n)]
		self.count = self.dfs(0, m)
	
	def dfs(self, row, chesses_left):
		if chesses_left == 0:
			return 1
		elif row == self.n:
			if chesses_left == 0:
				return 1
			else:
				return 0
		else:
			counts = 0
			for pos, val in enumerate(self.map[row]):
				if val == '#' and not self.cols[pos]:
					self.cols[pos] = True
					counts += self.dfs(row + 1, chesses_left - 1)
					self.cols[pos] = False
			counts += self.dfs(row + 1, chesses_left)
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

dfs = DFS(map_list, m)
print(dfs.count)