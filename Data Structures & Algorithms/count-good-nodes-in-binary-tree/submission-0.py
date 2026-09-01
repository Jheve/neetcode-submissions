# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # start with using bfs for traversal
        # easy -> keep updating maximum value so far for each path
        q = deque()
        result = 0

        # initialize queue with (root, maxValue) pair
        q.append((root, -float('inf')))

        while q:
            node, maxValue = q.popleft()

            # increase good node count if node is greater than max
            if node.val >= maxValue:
                result += 1
            
            # check left and right children and add them to queue
            if node.left:
                q.append((node.left, max(maxValue, node.val)))
            
            if node.right:
                q.append((node.right, max(maxValue, node.val)))
            
        
        return result


        