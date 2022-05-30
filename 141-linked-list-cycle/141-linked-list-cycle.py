# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        
        while fast and fast.next: # have to use fast and fast.next so that you can use fast.next.next
            slow = slow.next      # basically both will cycle, and if it keeps going 
            fast = fast.next.next # fast eventually catches up and timing's slow
            
            if slow == fast:
                return True
            
        return False
            
        