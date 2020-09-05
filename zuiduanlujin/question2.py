class Item(object):
	def __init__(self, v_index, value):
		self.v_index = v_index
		self.value = value

	def __lt__(self, other):
		return self.value < other.value
		

class Heap(object):
	def __init__(self):
		self.__items = [None]
		self.__size = 0

	def add(self, v, x):
		self.__size += 1
		item = Item(v, x)
		self.__items.append(item)
		self.__swim_up(self.__size)

	def change_priority(self, v, x):
		for index, item in enumerate(self.__items):
			if item is not None:
				if item.v_index == v:
					item.value = x
					self.__swim_up(index)
					self.__swim_down(index)
					break

	def get_smallest(self):
		return self.__items[1].v_index, self.__items[1].value

	def remove_smallest(self):
		self.__size -= 1
		if self.__size > 0:
			self.__items[1] = self.__items.pop()
		else:
			item = self.__items.pop()
		self.__swim_down(1)

	def size(self):
		return self.__size

	def __swim_up(self, index):
		if index == 1:
			return

		parent_index = index // 2
		if self.__items[index] < self.__items[parent_index]:
			self.__swap(index, parent_index)
			self.__swim_up(parent_index)

	def __swim_down(self, index):
		left_child_index = index * 2
		right_child_index = index * 2 + 1
		swim_down_index = index

		if left_child_index <= self.__size:
			if self.__items[left_child_index] < self.__items[index]:
				swim_down_index = left_child_index

		if right_child_index <= self.__size:
			if self.__items[right_child_index] < self.__items[index]:
				if self.__items[right_child_index] < self.__items[left_child_index]:
					swim_down_index = right_child_index

		if swim_down_index != index:
			self.__swap(index, swim_down_index)
			self.__swim_down(swim_down_index)

	def __swap(self, a, b):
		self.__items[a], self.__items[b] = self.__items[b], self.__items[a]

	def __str__(self):
		return str([(i.v_index, i.value) for i in self.__items[1:]])

class Graph(object):
	def __init__(self, vertices, directed):
		self.vertices = vertices
		self.directed = directed
		self.adj = [{} for _ in range(vertices)]

	def add_edge(self, v, w, dist):
		self.adj[v][w] = dist
		if not self.directed:
			self.adj[w][v] = dist

	def get_adj(self, v):
		return self.adj[v]

	def get_dist(self, v, w):
		return self.adj[v][w]

	def get_v_nums(self):
		return self.vertices

class Dijkstra(object):
	def __init__(self, g, s):
		self.graph = g
		self.s = s
		self.dist_to = [float('inf') for _ in range(g.get_v_nums())]
		self.dist_to[self.s] = 0
		self.edge_to = [None for _ in range(g.get_v_nums())]
		self.fringe = Heap()
		for i in range(self.graph.get_v_nums()):
			if i != self.s:
				self.fringe.add(i, float('inf'))
			else:
				self.fringe.add(i, 0)

		self.run()

	def run(self):
		while self.fringe.size() > 0:
			v, dist = self.fringe.get_smallest()
			self.fringe.remove_smallest()
			for w in self.graph.get_adj(v):
				dist = self.graph.get_dist(v, w)
				if dist + self.dist_to[v] < self.dist_to[w]:
					self.dist_to[w] = dist + self.dist_to[v]
					self.edge_to[w] = v
					self.fringe.change_priority(w, dist + self.dist_to[v])


	def get_shortest_path_to(self, v):
		path = [v]
		while v != self.s:
			v = self.edge_to[v]
			path.insert(0, v)
		return path

n, m = input().split(' ')
n = int(n)
m = int(m)
graph = Graph(n, False)
for _ in range(m):
	s_input = input()
	v, w, cost = s_input.split(' ')
	graph.add_edge(int(v) - 1, int(w) - 1, int(cost))

dijkstra = Dijkstra(graph, 0)
max_days = max(dijkstra.dist_to)
if max_days == float('inf'):
	print(-1)
else:
	print(max_days)