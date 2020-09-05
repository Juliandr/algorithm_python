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
		k = k.lower()
		node = self.root
		for letter in k:
			if letter not in node.children:
				return False
			else:
				node = node.children[letter]
		return node.is_key

	def __collect_help(self, s, n):
		result = []
		if n.is_key:
			result.append(s)
		for child in n.children:
			result.extend(self.__collect_help(s + child, n.children[child]))
		return result

	def get_keys_with_prefix(self, k):
		result = []
		node = self.root
		for letter in k:
			if letter in node.children:
				node = node.children[letter]
			else:
				return result
		if node.is_key:
			result.append(k)
		for child in node.children:
			child_node = node.children[child]
			result.extend(self.__collect_help(k + child, child_node))

		return result

s = input().split(' ')
trie = BasicTrieSet()
for word in s:
	trie.add(word)
to_find = input()
result = trie.get_keys_with_prefix(to_find)
result.sort()
print(' '.join(result))