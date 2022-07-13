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
        queue.append(root) # length of queue starts at one
        
        while queue: # each level
            queueLen = len(queue)
            levelList = []
            for i in range(queueLen): # the nodes in each level
                node = queue.popleft()
                # check for non-null
                if node: # even if queue appends None, it won't append it to the whole levelList
                    levelList.append(node.val)
        # populate the queue with left and right children to eventually explore on next iteration
                    queue.append(node.left) 
                    queue.append(node.right)
            if levelList: # check for non-null levels to append
                res.append(levelList)
        return res
        