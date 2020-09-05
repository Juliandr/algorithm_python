class DepthFirstIslands(object):
	def __init__(self, map_list):
		self.map = map_list
		self.m = len(self.map)
		self.n = len(self.map[0])
		self.marked = [[False for _ in line] for line in self.map]
		self.count = 0
		for x in range(self.n):
			for y in range(self.m):
				if not self.marked[y][x]:
					if self.dfs(x, y):
						self.count += 1
	
	def dfs(self, x, y):
		if x<0 or x>=self.n or y<0 or y>=self.m:
			return False
		elif self.map[y][x] == 0:
			return False
		elif self.marked[y][x]:
			return False
		else:
			self.marked[y][x] = True
			self.dfs(x-1, y)
			self.dfs(x+1, y)
			self.dfs(x, y-1)
			self.dfs(x, y+1)
			return True


n = int(input())
map_list = [[] for _ in range(n)]
for i in range(n):
	s_input = input()
	for l in s_input:
		map_list[i].append(int(l))

# map_list = [[1, 1, 0, 0, 0], [1, 1, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 1, 1]]
dfi = DepthFirstIslands(map_list)
print(dfi.count)