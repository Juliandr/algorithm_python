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


s = input().split(' ')
seq = [int(i) for i in s]
mss = MaxSubSeq(seq)
print(mss.get_ans(len(seq)))