# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # bfs queue
        # queue.append()
        # queue.popleft()
        # pick a root, add to queue
        # pop the root from queue
        # then add left and right to queue
        # then pop left from queue and explore its left and right
        # then pop right from queue and explore its left and right
        
        res = []
        
        queue = collections.deque()
        queue.append(root)
        
        while queue:
            queueLen = len(queue)
            levelList = []
            for i in range(queueLen):
                node = queue.popleft()
                # check for non-null
                if node: # even if queue appends None, it won't append it to the whole levelList
                    levelList.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
            if levelList: # check for non-null levels
                res.append(levelList)
        return res
        