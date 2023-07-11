# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        p1 = headA
        while p1.next is not None:
            p1 = p1.next
        p1.next = headB
        # Detect a cycle if none exists then fast is none
        # then return
        fast = headA
        slow = headA
        
        while fast is not None:
            if fast.next is None or fast.next.next is None:
                fast = None
                break
            
            fast = fast.next.next
            slow = slow.next
            if fast is slow:
                break
    
        
        if fast is None:
            p1.next = None
            return None
        # count the cycle
        count = 1
   
        # return ListNode(0)
        slow = slow.next
        while fast is not slow:
            slow = slow.next
            count += 1
        
      
        # finish
        still = headA
        slow = headA
        move_count = 0
        while move_count < count:
            move_count += 1
            slow = slow.next
        while still is not slow:
            still = still.next
            slow = slow.next
        p1.next = None
        return slow
        