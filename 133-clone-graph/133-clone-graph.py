"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        oldToNew = {}
        
        def clonedfs(node): # node that we are visiting
            if node in oldToNew: # already made a clone of the node
                return oldToNew[node] # return the already made clone
            
            copy = Node(node.val) # copy the node using same value
            oldToNew[node] = copy # put in hashmap
            for neighbor in node.neighbors: # iterate through original node's neighbors
                copy.neighbors.append(clonedfs(neighbor)) # append all neighbors
            return copy
        
        return clonedfs(node) if node else None # for null case