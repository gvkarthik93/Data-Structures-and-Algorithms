def traverse(root):
	
	stack = []

	current = root

	while current is not None or len(stack)>0:
		if current is not None:
			stack.append(current)
			current = current.left

		else:
			current = stack.pop()
			print (current.data)
			current = current.right