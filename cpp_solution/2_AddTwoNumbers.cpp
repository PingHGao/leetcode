/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        int sum = 0;
        ListNode *res = new ListNode(0);
        ListNode *cur = res;
        
        while(1) {
            if (l1 != NULL){
                sum += l1->val;
                l1 = l1->next;
            }
            if (l2 != NULL){
                sum += l2->val;
                l2 = l2->next;
            }
            
            cur->val = sum % 10;
            sum /= 10;
            
            if (l1 != NULL || l2 != NULL || sum){
                cur->next = new ListNode(0);
                cur = cur->next;
            }
            else
                break;
        }
        
        return res;
    }
};
