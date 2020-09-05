s = input()

s_list = s.split(' ')
stack = []
can_match =True
for item in s_list:
	if item[0] == 'm':
		stack.append(item)
	else:
		if len(stack)==0:
			can_match = False
			break
		else:
			if stack[-1][1] == item[1]:
				stack.pop()
if len(stack)>0:
	can_match = False
print(can_match)