# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        a, b = headA, headB
        
        while a != b:
            if a: # while not null
                a = a.next 
            else: # after it reaches end of list
                a = headB
            if b: 
                b = b.next
            else:
                b = headA
        return a # doesn't matter cause a or b = intersection or null
        
        