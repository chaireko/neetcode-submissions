# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # divide list in half
        # iterate through first list
        # iterate backwards through second list
        # GET MIDPOINT
        fast = head.next
        slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        curr, prev = slow.next, None
        slow.next = None
        # REVERSE L2
        while curr:
            next_ = curr.next
            curr.next = prev
            prev = curr
            curr = next_
        l1, l2 = head, prev
        # COMBINE LISTS
        while l2:
            tmp1, tmp2 = l1.next, l2.next
            l1.next = l2
            l2.next = tmp1
            l1 = tmp1
            l2 = tmp2


