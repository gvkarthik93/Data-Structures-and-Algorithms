class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return
        if root == p or root == q:
            return root
        leftnode = self.lowestCommonAncestor(root.left,p,q)
        rightnode = self.lowestCommonAncestor(root.right,p,q)
        
        if rightnode is not None and leftnode is not None:
            return root
        if rightnode is None and leftnode is None:
            return None
        
        return leftnode if leftnode is not None else rightnode