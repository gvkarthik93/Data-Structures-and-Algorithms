def traverse(root):
	
	stack = []

	current = root

	while True:
		if current is not None:
			stack.append(current)
			current = current.left

		else:
			if len(stack) > 0:
				current = stack.pop()
				print (current.data)
				current = current.right
			else:
				break