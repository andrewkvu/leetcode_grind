# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        l1, l2, res = [], [], []
        self.dfs(l1, root1)
        self.dfs(l2, root2)
        for num in l1:
            res.append(num)
        for num in l2:
            res.append(num)
        return sorted(res)
        
    def dfs(self, l, root):
        if root:
            l.append(root.val)
            self.dfs(l, root.left)
            self.dfs(l, root.right)