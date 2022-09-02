# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        # BFS queue
        res = []
        queue = collections.deque()
        queue.append(root)
        
        while queue:
            queueLen = len(queue)
            levelList = []
            for i in range(queueLen):
                node = queue.popleft()
                if node:
                    levelList.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
            if levelList:
                res.append(sum(levelList) / len(levelList))
        
        return res