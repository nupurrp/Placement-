# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
         h1 = head
         mid = self.findMiddle(h1)
         h2 = mid.next
         mid.next = None
         h1 = self.reverse(h1)
         return self.checkPallindrom(h1, h2) or self.checkPallindrom(h1.next, h2)
    
    def findMiddle(self, root):
        s1, s2 = root, root
        while s2.next and s2.next.next:
            s1 = s1.next
            s2 = s2.next.next
        return s1  # int(s2.next == None)
    
    def checkPallindrom(self, root1, root2):
        while root1 or root2:
            if root1 == None or root2 == None:
                return False
            if root1.val != root2.val:
                return False
            root1 = root1.next
            root2 = root2.next
        return True
    
    def reverse(self, root):
        pre = None
        cur = root
        while cur:
            post = cur.next
            cur.next = pre
            pre = cur
            cur = post
        return pre

        