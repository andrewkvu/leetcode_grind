# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        n = 0 # number of elements visited so far in the tree
        stack = []
        cur = root
        
        while cur or stack:
            while cur: # want to go far left
                stack.append(cur) # want to go back to cur after going far left
                cur = cur.left
            
            cur = stack.pop() # after cur is null means we can process the last node
            n += 1
            if n == k: # kth smallest
                return cur.val
            cur = cur.right # if the other cases don't work, move on to the right subtree 
        