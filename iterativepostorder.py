def peek(stack):
    if len(stack) > 0:
        return stack[-1]
    return None
# A iterative function to do postorder traversal of 
# a given binary tree
def postOrderIterative(root):
         
    # Check for empty tree
    if root is None:
        return
 
    stack = []
     
    while(True):
        while (root):
            # Push root's right child and then root to stack
            if root.right is not None:
                stack.append(root.right)
            stack.append(root)
 
             # Set root as root's left child
            root = root.left
         
        # Pop an item from stack and set it as root
        root = stack.pop()
 
        # If the popped item has a right child and the
        # right child is not processed yet, then make sure
        # right child is processed before root
        if (root.right is not None and
            root.right == peek(stack)):
            stack.pop() # Remove right child from stack 
            stack.append(root) # Push root back to stack
            root = root.right # change root so that the 
                             # righ child is processed next
 
        # Else print root's data and set root as None
        else:
            ans.append(root.data) 
            root = None
 
        if (len(stack) <= 0):
                break