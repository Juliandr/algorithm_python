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

	def contains(self, k):
		if '*' in k:
			return self.__fuzzy_contains(k, self.root)
		else:
			k = k.lower()
			node = self.root
			for letter in k:
				if letter not in node.children:
					return False
				else:
					node = node.children[letter]
			return node.is_key

	def __fuzzy_contains(self, k, n):
		if len(k) == 0:
			return n.is_key
		elif k[0] == '*':
			for child in n.children:
				child_node = n.children[child]
				if self.__fuzzy_contains(k[1:], child_node):
					return True
			return False
		elif k[0] in n.children:
			return self.__fuzzy_contains(k[1:], n.children[k[0]])
		else:
			return False

s = input().split(' ')
trie = BasicTrieSet()
for word in s:
	trie.add(word)

find_word_list = input().split(' ')
result = []
for word in find_word_list:
	result.append(str(trie.contains(word)))
result = ' '.join(result)
print(result)

# trie = BasicTrieSet()
# trie.add('sad')
# trie.add('sam')
# trie.add('sample')
# trie.add('spy')
# trie.add('spite')
# print(trie.contains('s**ple'))