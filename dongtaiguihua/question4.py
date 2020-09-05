class SimilarGenes(object):
	def __init__(self, gene1, gene2):
		self.gene1 = gene1
		self.gene2 = gene2
		self.similar_score = {
			'A': {'A': 5, 'C': -1, 'G': -2, 'T': -1, '-': -3},
			'C': {'A': -1, 'C': 5, 'G': -3, 'T': -2, '-': -4},
			'G': {'A': -2, 'C': -3, 'G': 5, 'T': -2, '-': -2},
			'T': {'A': -1, 'C': -2, 'G': -2, 'T': 5, '-': -1},
			'-': {'A': -3, 'C': -4, 'G': -2, 'T': -1, '-': 0}
		}
		self.ans = [[None for _ in range(len(gene2) + 1)] for _ in range(len(gene1) + 1)]
		self.result = self.dp(len(gene1), len(gene2))

	def dp(self, g1i, g2i):
		if self.ans[g1i][g2i]:
			return self.ans[g1i][g2i]
		elif g1i == 0 and g2i == 0:
			return 0
		elif g1i == 0:
			self.ans[g1i][g2i] = self.get_similar_score('-', self.gene2[g2i-1])
			if g2i > 1:
				self.ans[g1i][g2i] += self.dp(g1i, g2i - 1)
			return self.ans[g1i][g2i]
		elif g2i == 0:
			self.ans[g1i][g2i] = self.get_similar_score(self.gene1[g1i-1], '-')
			if g1i > 1:
				self.ans[g1i][g2i] += self.dp(g1i - 1, g2i)
			return self.ans[g1i][g2i]
		else:
			# 匹配情况1：gene1取空和gene2配对
			score1 = self.dp(g1i, g2i - 1) + self.get_similar_score('-', self.gene2[g2i-1])
			# 匹配情况2：gene2取空和gene1配对
			score2 = self.dp(g1i - 1, g2i) + self.get_similar_score(self.gene1[g1i-1], '-')
			# 匹配情况3：gene1和gene2直接配对
			score3 = self.dp(g1i - 1, g2i - 1) + self.get_similar_score(self.gene1[g1i-1], self.gene2[g2i-1])
			self.ans[g1i][g2i] = max(score1, score2, score3)
			return self.ans[g1i][g2i]


	def get_similar_score(self, g1, g2):
		return self.similar_score[g1][g2]

# gene1 = 'AGCTATT'
# gene2 = 'AGCTTTAAA'
# gene1 = 'A'
# gene2 = 'A'
# gene1 = 'ATT'
# gene2 = 'TTAAA'
# gene1 = 'A'
# gene2 = 'TTA'
gene1 = input()
gene2 = input()
similar_gene = SimilarGenes(gene1, gene2)
print(similar_gene.result)