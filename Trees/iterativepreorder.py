def traverse(root):
	if root is None:
		return

	stack = []

	stack.append(root)

	while len(stack) > 0:
		node = stack.pop()

		print (node.data)

		if node.right is not None:
			stack.append(node.right)

		if node.left is not None:
			stack.append(node.left)
