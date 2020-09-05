class Graph(object):
	def __init__(self, vertices):
		self.vertices = vertices
		self.adj = [[] for _ in range(vertices)]

	def add_edge(self, v, w):
		self.adj[v].append(w)

	def get_adj(self, v):
		return self.adj[v]

	def get_v_nums(self):
		return self.vertices

class DepthFirstPaths(object):
	def __init__(self, g, s):
		self.g = g
		self.s = s
		self.has_cycle = False
		self.marked = [False for _ in range(g.get_v_nums())]
		self.to_v = []
		self.dfs(g, s)
	
	def dfs(self, g, v):
		self.marked[v] = True
		for w in g.get_adj(v):
			if not self.marked[w]:
				self.to_v.append(w)
				if not self.dfs(g, w):
					return False
			else:
				# 如果能走到一个之前标记过的节点说明存在环
				# 发现存在环的情况就没必要做更多计算
				# 直接退出递归
				self.has_cycle = True
				return False
		return True

	def has_path_to_all(self):
		# 如果所有节点都能到达则
		# self.to_v长度应该是图节点数-1（-1是要去掉起始点）
		if len(self.to_v) == self.g.get_v_nums() - 1 and not self.has_cycle:
			return True
		else:
			return False

n = int(input())
players = dict()
records = []
winners = set()
losers = set()
for _ in range(n):
	s_input = input()
	s_list = s_input.split(' ')
	records.append(s_list)
	winner, loser = s_list
	if winner not in players:
		players[winner] = len(players)
	if loser not in players:
		players[loser] = len(players)

	# 所有记录中的赢家和输家都加入到集合里
	# 赢家集合-输家集合=完全无败绩的选手
	winners.add(winner)
	losers.add(loser)

graph = Graph(len(players))
for winner, loser in records:
	graph.add_edge(players[winner], players[loser])

true_winners = winners - losers
has_final_winner = False
for winner in true_winners:
	dfp = DepthFirstPaths(graph, players[winner])
	if dfp.has_path_to_all():
		has_final_winner = True
		break
print(has_final_winner)