# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []
        
        def dfs(node, path, currSum):
            temp = path + [node.val]
            if node.left:
                dfs(node.left, temp, currSum - node.val)
            if node.right:
                dfs(node.right, temp, currSum - node.val)
            if not node.left and not node.right and currSum == node.val:
                res.append(temp)
            
        if not root:
            return []
        dfs(root, [], targetSum)
        return res
        
        