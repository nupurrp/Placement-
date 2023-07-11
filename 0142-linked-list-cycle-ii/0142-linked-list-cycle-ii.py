# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nodespresent= set()
        node=head

        while node is not None:
            if node in nodespresent:
                return node    
            else:
                nodespresent.add(node)  
                node=node.next
        return None
        