# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        # BFS queue level order traversal
        # pick a root, add to queue
        # pop root from the queue
        # add left and right to queue
        # pop left from queue and explore its left and right
        # pop right from queue and explore its left and right
        queue = deque()
        res = []
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
                res.append(levelList)
        
        return res[::-1]
            