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
        
        if root.val > p and root.val > q:
            return self.lowestCommonAncestor(root.left, p, q)

        elif root.val < p and root.val < q:
            return self.lowestCommonAncestor(root.right, p, q)

        else:
            return root