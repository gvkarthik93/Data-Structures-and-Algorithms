class Node:
    def __init__(self, key, value):
        self.key = key
        self.val = value
        self.count = 1
        self.prev = None
        self.next = None

class DLL:
    def __init__(self):
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0
        
    
    def insertToFront(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node
        self.size += 1
    
    def remove(self, node):
        prevnode = node.prev
        nextnode = node.next
        prevnode.next = nextnode
        nextnode.prev = prevnode
        self.size -= 1

class LFUCache(object):

    def __init__(self, size):
        """
        :type capacity: int
        """        
        self.capacity = size
        self.leastCount = 1e9
        self.nodeMap = {}
        self.countMap = {}

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.nodeMap:
            node = self.nodeMap[key]
            self.promote(node)
            return node.val
        else:
            return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        
        if key in self.nodeMap:
            node = self.nodeMap[key]
            node.val = value
            self.promote(node)
            return
        
        if self.capacity == 0:
            return
        
        if len(self.nodeMap) == self.capacity:
            self.removeLeastCountNode()
        
        node = Node(key, value)
        self.nodeMap[key] = node
        
        if node.count in self.countMap:
            self.countMap[node.count].insertToFront(node)
        else:
            self.countMap[node.count] = DLL()
            self.countMap[node.count].insertToFront(node)
        
        self.leastCount = 1
        
    def removeLeastCountNode(self):
        lst = self.countMap[self.leastCount]
        lastnode = lst.tail.prev
        lst.remove(lastnode)
        del self.nodeMap[lastnode.key]
            
    def promote(self, node):
        lst = self.countMap[node.count]
        lst.remove(node)
        
        if self.leastCount == node.count and lst.size == 0:
            self.leastCount += 1
        
        node.count += 1
        if node.count in self.countMap:
            self.countMap[node.count].insertToFront(node)
        else:
            self.countMap[node.count] = DLL()
            self.countMap[node.count].insertToFront(node)


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)