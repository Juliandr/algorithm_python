def move(x, y):
	if x == n-1 and y == n-1:
		return 1
	else:
		count = 0
		if x+1<n:
			if city_map[x+1][y]==0:
				count += move(x+1, y)
		if y+1<n:
			if city_map[x][y+1]==0:
				count += move(x, y+1)

		return count

n = int(input())
city_map = []
for _ in range(n):
	s = input()
	line = s.split(' ')
	city_map.append([int(i) for i in line])

print(move(0, 0))