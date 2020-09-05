class Graph(object):
	def __init__(self, vertices, directed):
		self.vertices = vertices
		self.directed = directed
		self.adj = [[] for _ in range(vertices)]

	def add_edge(self, v, w):
		self.adj[v].append(w)
		if not self.directed:
			self.adj[w].append(v)

	def get_adj(self, v):

		# 对邻接节点进行倒序排序
		# 保证最终结果里小的在前面
		self.adj[v].sort(reverse=True)
		return self.adj[v]

	def get_v_nums(self):
		return self.vertices

class DepthFirstOrder(object):
	def __init__(self, g):
		self.g = g
		self.reverse_postorder = []
		self.marked = [False for _ in range(g.get_v_nums())]

		# 倒序进行dfs才能保证最终结果里小的在前面
		for v in range(g.get_v_nums() - 1, -1, -1):
			if not self.marked[v]:
				self.dfs(self.g, v)

	def dfs(self, g, v):
		self.marked[v] = True
		for w in g.get_adj(v):
			if not self.marked[w]:
				self.dfs(self.g, w)
		self.reverse_postorder.insert(0, v)

	def get_reverse_postorder(self):
		self.reverse_postorder = [i + 1 for i in self.reverse_postorder]
		return self.reverse_postorder

n, m = input().split(' ')
n = int(n)
m = int(m)
records = []
for _ in range(m):
	s_input = input()
	s_list = s_input.split(' ')
	records.append(s_list)

graph = Graph(n, True)
for winner, loser in records:
	graph.add_edge(int(winner) - 1, int(loser) - 1)

dfo = DepthFirstOrder(graph)
answer = [str(i) for i in dfo.get_reverse_postorder()]
print(' '.join(answer))