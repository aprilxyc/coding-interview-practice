def balanced_parenthesis(s):
	stack = [] 
	pairs = {'(':')', '[':']', '{':'}'}

	if len(stack) == 0:
		return False

	for char in s:
		if char in pairs:
			stack.append(char)
			print("hello")
		else:
			print("hello")
			popped_bracket = stack.pop()
			if char != pairs[popped_bracket]:
				return False

	if len(stack) != 0:
		return False
	return True
	
print(balanced_parenthesis("()[]{}"))
	  