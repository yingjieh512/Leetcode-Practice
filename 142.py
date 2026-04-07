# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow=head
        if slow==None:
            return None
        fast=head
        while True:
            if fast==None or fast.next==None:
                return None
            fast=fast.next.next
            slow=slow.next
            if fast==slow:
                fast=head
                break
        while True:
            if fast==slow:
                return fast
            fast=fast.next
            slow=slow.next
            
            
