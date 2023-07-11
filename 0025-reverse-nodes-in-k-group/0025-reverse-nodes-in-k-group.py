# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
         dummy = ListNode(0, head)
         grpPrev = dummy
         while True:
             kth = self._findKth(grpPrev, k)
             if not kth:
                 break
             grpNext = kth.next
             prev, cur = kth.next, grpPrev.next
             while cur != grpNext:
                 nxt = cur.next
                 cur.next = prev
                 prev = cur
                 cur = nxt

             tmp = grpPrev.next
             grpPrev.next = kth
             grpPrev = tmp

         return dummy.next

    def _findKth(self,curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr
                
        