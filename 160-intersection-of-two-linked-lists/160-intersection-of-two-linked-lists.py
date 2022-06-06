# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        hset = set()
        tempA = headA
        tempB = headB
        while tempA:
            hset.add(tempA)
            tempA = tempA.next
        
        while tempB:
            if tempB in hset:
                return tempB
            tempB = tempB.next
        
        