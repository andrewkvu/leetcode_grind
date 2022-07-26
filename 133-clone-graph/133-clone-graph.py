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
                # ie 1 has neighbors 2 and 4, function will create copies of 2 and 4
                # and append its neighbors, etc, etc until it gets to the last node
                # then it will recursively go back to the first node called
            return copy
        
        return clonedfs(node) if node else None # for null case