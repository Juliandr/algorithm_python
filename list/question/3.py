def sub_sum(arr, index, target):
	if target == 0:
		return True
	elif index == 0:
		return arr[0] == target
	elif arr[index] > target:
		return sub_sum(arr, index - 1, target)
	else:
		return sub_sum(arr, index - 1, target - arr[index]) or sub_sum(arr, index - 1, target)


s = input().split(' ')
target = int(input())
array = [int(i) for i in s]
index = len(array) - 1
print(sub_sum(array, index, target))