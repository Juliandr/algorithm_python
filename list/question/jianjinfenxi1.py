import math

combination = []

def factorization(num, from_num):
	global combination
	if num==from_num:
		combination.append(str(num))
		output()
		combination.pop()
	elif num == 1:
		output()
	else:
		sqrt_n = int(math.sqrt(num))
		if from_num>2:
			start_num = from_num
		else:
			start_num = 2
		for i in range(start_num, sqrt_n+1):
			if num%i==0:
				combination.append(str(i))
				factorization(int(num/i), i)
				combination.pop()
		combination.append(str(num))
		output()
		combination.pop()

def output():
	s = '{}='.format(n)
	s += '*'.join(combination)
	print(s)


n = int(input())
factorization(n, 1)

#渐近分析答案 1.BAFEIDHGC 2. TFTFTTF