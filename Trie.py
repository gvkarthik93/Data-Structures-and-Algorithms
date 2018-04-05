
class Node():
	def __init__(self):
		self.children = dict()
		self.endOfWord = False

def insert(word):
	current = root
	for i in range(len(word)):
		ch = word[i]
		node = current.children.get(ch, None)
		if node is None:
			node = Node()
			current.children[ch] = node
		current = node
	current.endOfWord = True

def search(word):
	current = root
	for i in range(len(word)):
		ch = word[i]
		node = current.children.get(ch, None)
		if not node:
			return False
		current = node
	return current.endOfWord

def delete(current, word, index):
	if index == len(word):
		if not current.endOfWord:
			return False
		current.endOfWord = False
		return len(current.children) == 0
	ch = word[index]
	node = current.children.get(ch, None)
	if node is None:
		return False
	shouldDeleteCurrentNode = delete(node, word, index+1)
	if shouldDeleteCurrentNode:
		del current.children[ch]
		return len(current.children) == 0
	return False

root = Node()
insert("HOLA")
print (search("HOLA"))
print (delete(root, "HOLAA", 0))
print (search("HOLA"))