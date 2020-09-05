def anagrams(strs):
	word_dict = {}
	for word in strs:
		sorted_word = ' '.join(sorted(word))
		if sorted_word not in word_dict:
			word_dict[sorted_word] = [word]
		else:
			word_dict[sorted_word].append(word)

		count = 0
		for item in word_dict:
			if len(word_dict[item]) >= 2:
				count += 1
		return count

s = input()
word_list = s.split(' ')
print(anagrams(word_list))