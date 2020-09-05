def letter_num(c):
	return ord(c) - 96



def english_to_int(s):
	int_rep = 0
	for c in s:
		int_rep = int_rep * 27
		int_rep = int_rep + letter_num(c)
	return int_rep

print(english_to_int('bee'))