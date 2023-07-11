/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* middleNode(ListNode* head) {
       ListNode*curr = head;
        ListNode*temp=head;
          if(temp->next==NULL)
            return curr;
            if(temp->next->next==NULL)
            return curr->next;
            
        while(temp){
            temp=temp->next;
            temp=temp->next;
            curr=curr->next;
              if(temp->next==NULL)
            return curr;
            if(temp->next->next==NULL)
            return curr->next;
        }
        return curr;  
    }
};