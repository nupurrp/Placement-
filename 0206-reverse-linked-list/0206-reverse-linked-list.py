# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None # there is no previous node
        curr = head # the head of the linked list, representing the current node we are working with 

        while curr:# iteration stops when curr becomes None(reach the end of the original list)
            next_node = curr.next # store the reference to the next node so we don't lose the reference to the remaining part of the original list
            curr.next = prev # update the next pointer of the current node to point to the previous node 
            
            # prepares us for the next iteration of the loop, where we reverse the pointer of the next node.
            prev = curr # move prev one step forward
            curr = next_node # move curr one step forward

        return prev