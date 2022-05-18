class Node():

    def __init__(self, data):
        self.key = data
        self.left = None
        self.right = None


def insert(temp,key):

    if not temp:
        root = newNode(key)
        return
    q = []
    q.append(temp)

    # Do level order traversal until we find
    # an empty place.
    while (len(q)):
        temp = q[0]
        q.pop(0)

        if (not temp.left):
            temp.left = Node(key)
            break
        else:
            q.append(temp.left)

        if (not temp.right):
            temp.right = Node(key)
            break
        else:
            q.append(temp.right)

# Driver code
if __name__ == '__main__':
    root = Node(10)
    root.left = Node(11)
    root.left.left = Node(7)
    root.right = Node(9)
    root.right.left = Node(15)
    root.right.right = Node(8)


    key = 12
    insert(root, key)