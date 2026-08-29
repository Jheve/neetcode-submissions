# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # nested helper dfs function for tree traversal (children before cur node)
        def dfs(root):
            if not root:
                return [True, 0]
            
            # recursively check left and right subtrees
            leftSub = dfs(root.left)
            rightSub = dfs(root.right)

            # three conditions for balanced:
            # left subtree is balanced
            # right subtree is balanced
            # heights of the subtrees differ by at most 1
            isBalanced = (leftSub[0] and rightSub[0] and 
                         abs(leftSub[1] - rightSub[1]) <= 1)
            
            return [isBalanced, 1 + max(leftSub[1], rightSub[1])]
        
        return dfs(root)[0]