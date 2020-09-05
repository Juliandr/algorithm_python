class MaxHeap(object):
	def __init__(self):
		self.__keys = [None]
		self.__size = 0

	def add(self, x):
		self.__keys.append(x)
		self.__size += 1
		self.__swim_up(self.__size)

	def get_biggest(self):
		if self.__size > 0:
			return self.__keys[1]
		else:
			return None


	def remove_biggest(self):
		if self.__size > 1:
			self.__keys[1] = self.__keys.pop()
			self.__size -= 1
			self.__swim_down(1)
		elif self.__size > 0:
			self.__keys.pop()
			self.__size -= 1

	def size(self):
		return self.__size


	def __swim_up(self, index):
		if index == 1:
			return 
		parent_index = index // 2
		if self.__keys[parent_index] < self.__keys[index]:
			self.__swap(index, parent_index)
			self.__swim_up(parent_index)

	def __swim_down(self, index):
		left_child_index = index * 2
		right_child_index = index * 2 + 1 
		swim_down_index = index

		if left_child_index <= self.__size:
			if self.__keys[index] < self.__keys[left_child_index]:
				swim_down_index = left_child_index

		if right_child_index <= self.__size:
			if self.__keys[index] < self.__keys[right_child_index]:
				if self.__keys[left_child_index] < self.__keys[right_child_index]:
					swim_down_index = right_child_index

		if swim_down_index != index:
			self.__swap(index, swim_down_index)
			self.__swim_down(swim_down_index)


	def __swap(self, a, b):
		self.__keys[a], self.__keys[b] = self.__keys[b], self.__keys[a]

	def print(self):
		print(self.__keys[1:])
s = '3 1 2 4 5 3 2 6'
m = 3
heap = MaxHeap()
items = s.split(' ')
for item in items:
	if heap.size() < m:
		heap.add(int(item))
	elif int(item) < heap.get_biggest():
		heap.remove_biggest()
		heap.add(int(item))

s = ''
while heap.get_biggest() is not None:
	s += str(heap.get_biggest()) + ' '
	heap.remove_biggest()
print(s)