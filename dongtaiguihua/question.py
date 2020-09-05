class KnapSack(object):
	def __init__(self, w_list, v_list, max_w):
		self.w_list = w_list
		self.v_list = v_list
		self.count = len(self.w_list)
		self.max_w = max_w
		self.m = [{} for _ in range(self.count)]
		self.dp(0, self.max_w)

	def dp(self, index, w_left):
		w = self.w_list[index]
		v = self.v_list[index]

		if w_left in self.m[index]:
			return self.m[index][w_left]
		elif index == self.count - 1:
			if w <= w_left:
				return v
			else:
				return 0
		else:
			if w <= w_left:
				pick_v = v + self.dp(index + 1, w_left - w)
				not_pick_v = self.dp(index + 1, w_left)
				max_v = max(pick_v, not_pick_v)
				self.m[index][w_left]  = max_v
				return max_v
			else:
				self.m[index][w_left] = self.dp(index + 1, w_left)
				return self.m[index][w_left]

	def get_max_v(self):
		return self.m[0][self.max_w]


max_w, n = input().split(' ')
max_w = int(max_w)
n = int(n)
if n > 0:
	w_list = input().split(' ')
	w_list = [int(item) for item in w_list]
	v_list = input().split(' ')
	v_list = [int(item) for item in v_list]
	knapsack = KnapSack(w_list, v_list, max_w)
	print(knapsack.get_max_v())
else:
	print(0)