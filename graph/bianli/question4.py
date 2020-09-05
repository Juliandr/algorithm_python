class BottleState(object):
	def __init__(self, x, y, z):
		self.bottles = [x, y, z]

	def pour(self, s, t):
		if self.bottles[s] < origin_volume[t] - self.bottles[t]:
			pour_volume = self.bottles[s]
		else:
			pour_volume = origin_volume[t] - self.bottles[t]
		new_bottle_state = self.bottles.copy()
		new_bottle_state[s] -= pour_volume
		new_bottle_state[t] += pour_volume

		return BottleState(new_bottle_state[0],new_bottle_state[1],new_bottle_state[2])

	def get_tuple(self):
		return tuple(self.bottles)

	def __eq__(self, other):
		return self.bottles == other.bottles

	def __str__(self):
		return '({} {} {})'.format(self.bottles[0], self.bottles[1], self.bottles[2])


class BreadFirstPaths(object):
	def __init__(self, s, t):
		self.s = s
		self.t = t
		self.marked = []
		self.from_bs = []
		self.bfs(s, t)

	def bfs(self, s, t):
		self.fringe = []
		self.fringe.append(s)
		self.marked.append(s.get_tuple())
		self.from_bs.append(s)
		while self.fringe:
			# print([str(i) for i in self.fringe])
			v = self.fringe.pop(0)
			if v == self.t:
				break
			for s, t in zip([0,0,1,1,2,2], [1,2,0,2,0,1]):
				new_bottle_state = v.pour(s, t)
				if new_bottle_state.get_tuple() not in self.marked:
					self.marked.append(new_bottle_state.get_tuple())
					self.fringe.append(new_bottle_state)
					v_index = self.marked.index(v.get_tuple())
					self.from_bs.append(v_index)		

	def get_min(self):
		count = 0
		t_index = self.marked.index(self.t.get_tuple())
		while t_index > 0:
			count += 1
			t_index = self.from_bs[t_index]
		return count

	def get_path(self):
		path = []
		t_index = self.marked.index(self.t.get_tuple())
		while t_index > 0:
			path.insert(0, self.marked[t_index])
			t_index = self.from_bs[t_index]
		return path

b1, b2, b3 = input().split(' ')
b1 = int(b1)
b2 = int(b2)
b3 = int(b3)
target = b1 // 2
origin_volume = [b1, b2, b3]

start_bottle_state = BottleState(b1, 0, 0)
end_bottle_state = BottleState(target, target, 0)
bfp = BreadFirstPaths(start_bottle_state, end_bottle_state)
print(bfp.get_min())
# print(bfp.get_path())