# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # 0 n 1 n-1 2 n-2 3 n-3 4 n-4
        # to find the division of the two parts of the list
        # the part of 0 1 and n n-1
        slow = head
        fast = head.next
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # reversing the 2nd half of list
        begSecond = slow.next # slow is at the end of the 1st half, slow.next is beg of 2nd half
        slow.next = None # since slow is end of 1st half, it is where the reordered list should end
        prev = None
        
        while begSecond:
            temp = begSecond.next
            begSecond.next = prev
            prev = begSecond
            begSecond = temp
            
        # merge the two halves
        firstHead = head
        secondHead = prev # prev will be the beginning of the second list?
        while secondHead:
            tempNext = firstHead.next
            firstHead.next = secondHead
            firstHead = secondHead
            secondHead = tempNext
            