class Node:
	def __init__(self,key):
		self.val = key
		self.left = None
		self.right = None


class Tree:
	def insert(self, root, key):
		if root is None:
			return Node(key)

		else:
			if root.val == key:
				return root
		
			if key < root.val:
				root.left = self.insert(root.left, key)

			else:
				root.right = self.insert(root.right, key)
		
		return root

	def search(self, root, key):
		if root is None or root.val == key:
			return root

		if key < root.val:
			return self.search(root.left,key)

		return self.search(root.right,key)
 
 	def findMinElement(self, root):
 		current = root
 		while current.left is not none:
 			current = current.left
 		return current

	def delete(self, root, key):

		if root is None:
			return root

		if  key < root.val:
			root.left = self.delete(root.left, key)

		elif key > root.val:
			root.right = self.delete(root.right, key)

		else:
			if root.left is None:
				temp = root.right
				root = None
				return temp
			
			elif root.right is None:
				temp = root.left
				root = None
				return temp

			minNode = self.findMinElement(root.right)
			root.val = minNode.val
			self.delete(root.right, minNode.val)
		
		return root

	def inorder(self, root):
		if root is not None:
			self.inorder(root.left)
			print (root.val)
			self.inorder(root.right)

bsTree = Tree()
root = None
root = bsTree.insert(root, 50)
root = bsTree.insert(root, 30)
root = bsTree.insert(root, 20)
root = bsTree.insert(root, 40)
root = bsTree.insert(root, 70)
root = bsTree.insert(root, 60)
root = bsTree.insert(root, 80)

print ("Printing inorder")
bsTree.inorder(root)

print ("Delete a node")
bsTree.delete(root, 40)

print ("Search a node")
bsTree.search(root, 60)

print ("Printing inorder")
bsTree.inorder(root)