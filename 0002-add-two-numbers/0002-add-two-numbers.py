# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> 
    Optional[ListNode]:
        
        # Optimal one
        dummy = ListNode(0)
        curr = dummy
        carry = 0  # carry concept used

        while l1 or l2 or carry:  # l1 bacha ho ya l2 ya carry tab tk loop run kro
            if l1: # l1 ka value liya
                v1 = l1.val
            else:
