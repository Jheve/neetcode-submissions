# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # base case -> if no roots in either, subtree is in main tree
        if not subRoot:
            return True
        
        if not root:
            return False
        
        # call helper function to check if same root
        if self.isSameTree(root, subRoot):
            return True
        
        # use dfs to traverse tree
        return (self.isSubtree(root.left, subRoot) or
                self.isSubtree(root.right, subRoot))
    
    def isSameTree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True
        
        # traverse tree if roots match
        if root and subRoot and root.val == subRoot.val:
            return (self.isSameTree(root.left, subRoot.left) and
                    self.isSameTree(root.right, subRoot.right))
        
        return False
        

        