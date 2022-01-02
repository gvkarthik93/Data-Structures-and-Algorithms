class Node():
	def __init__(self):
		self.data = None
		self.next = None

class linked_list():
	def __init__(self):
		self.head = None

	def add_node(self, value):
		node = Node()
		node.data = value
		
		if self.head == None:
			self.head = node
			node.next = None

		else:
			current_node = self.head
			while current_node.next:
				current_node = current_node.next
			current_node.next = node
			node.next = None

	def list_print(self):
		node = self.head
		while node:
			print (node.data)
			node = node.next

ll = linked_list()
ll.add_node(1)
ll.add_node(2)
ll.add_node(3)

ll.list_print()

ll.add_node(10)
print ("Updated List")
ll.list_print()