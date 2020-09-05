class MaxSubSeq(object):
	def __init__(self, seq):
		self.seq = seq.copy()
		self.n = len(self.seq)
		self.ans = [None for _ in range(self.n)]
		self.ans[0] = self.seq[0]

		for i in range(1, self.n):
			self.ans[i] = max(self.ans[i-1] + self.seq[i], self.seq[i])

	def get_ans(self, i):
		return max(self.ans[:i])

class MaxSubMatrix(object):
	"""docstring for MaxSubMatrix"""
	def __init__(self, matrix):
		self.matrix = matrix.copy()
		self.rows = len(matrix)
		self.cols = len(matrix[0])
		self.ans = [[None for _ in range(self.cols)] for _ in range(self.rows)]

		# self.sum 保存的是从row行0列到row行col列所形成的序列数字之和
		self.sum = matrix.copy()
		for row in range(self.rows):
			for col in range(self.cols):
				if row > 0:
					self.sum[row][col] += self.sum[row-1][col]
		
		self.max_matrix_sum = -float('inf')
		for i in range(self.rows):
			for j in range(i, self.rows):
				self.ans = [None for _ in range(self.cols)]
				if i > 0:
					self.ans[0] = self.sum[j][0] - self.sum[i-1][0]
				else:
					self.ans[0] = self.sum[j][0]

				if self.ans[0] > self.max_matrix_sum:
					self.max_matrix_sum = self.ans[0]
				
				for k in range(1, self.cols):
					if i > 0:
						cur_sum = self.sum[j][k] - self.sum[i-1][k]
					else:
						cur_sum = self.sum[j][k]
					self.ans[k] = max(self.ans[k-1] + cur_sum, cur_sum)
					if self.ans[k] > self.max_matrix_sum:
						self.max_matrix_sum = self.ans[k]


	def get_ans(self):
		return self.max_matrix_sum

# matrix = [
# 	[0,-2,-7,0],
# 	[9,2,-6,2],
# 	[-4,1,-4,1],
# 	[-1,8,0,-2]
# ]
n = int(input())
matrix = []
for _ in range(n):
	s = input().split(' ')
	s = [int(i) for i in s]
	matrix.append(s)
msm = MaxSubMatrix(matrix)
print(msm.get_ans())