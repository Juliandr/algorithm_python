s = input()

stack = []
can_match =True
for item in s:
	if item == 'm':
		stack.append('m')
	else:
		if len(stack)==0:
			can_match = False
			break
		else:
			stack.pop()
if len(stack)>0:
	can_match = False
print(can_match)