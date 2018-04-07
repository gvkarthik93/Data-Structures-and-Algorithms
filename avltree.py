class Node:
	def __init__(self, data):
		self.data = data
		self.right = None
		self.left = None
		self.h = None

class AVLTree:
	def setHeight(self,root):
		return self.height(root)

	def leftRotate(self,root):
		newRoot = root.right
		root.right = newRoot.left
		newRoot.left = root
		newRoot.h = self.setHeight(newRoot)
		root.h = self.setHeight(root)
		return newRoot

	def rightRotate(self,root):
		newRoot = root.left
		root.left = newRoot.right
		newRoot.right = root
		newRoot.h = self.setHeight(newRoot)
		root.h = self.setHeight(root)
		return newRoot

	def balance(self,lroot, rroot):
		return self.height(lroot) - self.height(rroot)

	def height(self,root):
		if root is None:
			return 0
		return (1 + max((self.height(root.left) if root.left is not None else 0), (self.height(root.right) if root.right is not None else 0)))

	def insert(self, root, data):
		if root is None:
			return Node(data)
		if root.data < data:
			root.right = self.insert(root.right, data)
		else:
			root.left = self.insert(root.left, data)

		bal = self.balance(root.left, root.right)

		if bal > 1:
			if self.height(root.left.left) >= self.height(root.left.right):
				root = self.rightRotate(root)
			else:
				root.left = self.leftRotate(root.left);
				root = self.rightRotate(root);

		elif bal < -1:
			if self.height(root.right.right) >= self.height(root.right.left):
				root = self.leftRotate(root)
			else:
				root.right = self.rightRotate(root.right)
				root = self.leftRotate(root)

		else:
			root.h = self.setHeight(root)

		return root



avlTree = AVLTree()
root = Node(-10)
#root = avlTree.insert(root, -10);
root = avlTree.insert(root, 2);
root = avlTree.insert(root, 13);
root = avlTree.insert(root, -13);
root = avlTree.insert(root, -15);
root = avlTree.insert(root, 15);
root = avlTree.insert(root, 17);
root = avlTree.insert(root, 20);
