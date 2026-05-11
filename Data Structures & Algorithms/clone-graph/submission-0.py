"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # create map to store original graph nodes
        og_nodes = {}

        # conduct depth first search to prevent adding duplicate nodes (possible cycles)
        def dfs(node):
            # check if node is already stored
            if node in og_nodes:
                return og_nodes[node]

            # create copy node
            copy = Node(node.val)
            og_nodes[node] = copy

            # create copy node neighbors
            for neighbor in node.neighbors:
                copy.neighbors.append(dfs(neighbor)) 
            
            return copy
        
        if node:
            return dfs(node)
        else:
            return None