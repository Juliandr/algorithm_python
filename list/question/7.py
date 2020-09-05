combination = []

def permutation(arr, index, count):
	global combination
	if count == 1:
		for i in range(index+1, 0, -1):
			combination.append(i)
			print(combination)
			combination.pop()
	elif index>0:
		combination.append(arr[index])
		permutation(arr, index - 1, count- 1)
		combination.pop()
		permutation(arr, index - 1, count)

n = int(input())
m = int(input())
permutation([i for i in range(1, n+1)], n-1, m)


#渐近分析答案 1. D 2. FCEAF 3. F

