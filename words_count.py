words = []


def find_word_count(words):
	word_count = {}
	for word in set(words):
		word_count[word] = 0
	for word in words:
		word_count[word] += 1
	# for word in words:
	# 	if word in word_count:
	# 		word_count[word] += 1
	# 	else:
	# 		word_count[word] = 0
	#这里使用if不见得可以优化程序，但也是个选择

	return word_count



with open('i_have_a_dream.txt', 'r') as f:
	lines = f.readlines()#一次把所有东西都读进来，列表
	
	for line in lines:
		line.replace(',', ' ')
		line.replace('.', ' ')
		line.replace('"', ' ')
		line.replace('!', ' ')
		line.replace('?', ' ')
		line.replace(':', ' ')
		line.replace('\n', ' ')
		line.replace('-', ' ')

		for word in line.split(' '):
			if word:
				words.append(word)





print(find_word_count(words))
print("there is %d"%(len(words)))
print(len(set(words)))
