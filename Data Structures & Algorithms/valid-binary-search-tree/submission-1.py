# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def checkTree(node, left, right):
            if not node:
                return True

            # check if node val is between left and right nodes
            if not (left < node.val < right):
                return False
            
            # recursively validate left and right subtrees with updated range
            return checkTree(node.left, left, node.val) and checkTree(node.right, node.val, right)
        
        # initialize allowed range of root to infinity
        return checkTree(root, float("-inf"), float("inf"))
        

        

        
