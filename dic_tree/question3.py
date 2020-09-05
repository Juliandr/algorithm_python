class Graph(object):
	def __init__(self, vertices):
		self.vertices = vertices
		self.adj = [[] for _ in range(vertices)]
		self.in_degree = [0 for _ in range(vertices)]

	def add_edge(self, v, w):
		if w not in self.adj[v]:
			self.adj[v].append(w)
			self.in_degree[w] += 1

	def get_adj(self, v):
		return self.adj[v]

	def get_v_nums(self):
		return self.vertices

class BreadFirstSearch(object):
	def __init__(self, g):
		self.g = g   
		self.marked = [False for _ in range(g.get_v_nums())]
		self.graph_in_degree = self.g.in_degree.copy()
		self.has_cycle = self.check_cycle()
	
	def check_cycle(self):
		self.fringe = []
		for index, v_in_degree in enumerate(self.g.in_degree):
			if v_in_degree == 0:
				self.fringe.append(index)
		count = 0
		while self.fringe:
			v = self.fringe.pop()
			count += 1
			for w in self.g.adj[v]:
				self.graph_in_degree[w] -= 1
				if self.graph_in_degree[w] == 0:
					self.fringe.append(w)

		return not count == self.g.vertices

class Node(object):
	def __init__(self):
		self.children = {}
		self.is_key = False

class BasicTrieSet(object):
	def __init__(self):
		self.root = Node()

	def add(self, k):
		k = k.lower()
		node = self.root
		for letter in k:
			if letter not in node.children:
				child = Node()
				node.children[letter] = child
				node = child
			else:
				node = node.children[letter]
		node.is_key = True

	def check(self, k):
		self.graph = Graph(26)
		if not self.dfs(k, self.root):
			return False

		dfp = BreadFirstSearch(self.graph)
		if dfp.has_cycle:
			return False

		return True

	def dfs(self, k, n):
		if len(k) == 0:
			return True
		elif n.is_key:
			return False
		else:
			current_index = ord(k[0]) - ord('a')
			for child in n.children:
				child_index = ord(child) - ord('a')
				if current_index != child_index:
					self.graph.add_edge(current_index, child_index)
			return self.dfs(k[1:], n.children[k[0]])

s = input().split(' ')
trie = BasicTrieSet()
word_list = []
for word in s:
	trie.add(word)
	word_list.append(word)

# trie = BasicTrieSet()
# word_list = ['omm','moo','mom','ommnom']
# for word in word_list:
# 	trie.add(word)

result = []
for word in word_list:
	if trie.check(word):
		result.append(word)
result.sort()
print(' '.join(result))