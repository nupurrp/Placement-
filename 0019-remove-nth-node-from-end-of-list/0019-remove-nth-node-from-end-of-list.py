# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)

        left = dummy
        right = head

        while n > 0:                # Creates n-sized window
            right = right.next
            n -= 1
        

        while right:                # Moves the n-sized window into position
            right = right.next
            left = left.next

        left.next = left.next.next  # Remove nth node

        return dummy.next           # Return Head
        