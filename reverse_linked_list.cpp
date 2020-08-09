// https://leetcode.com/problems/reverse-linked-list/
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
    ListNode* reverseList(ListNode* head) {
        if(!head)
            return head;
        
        ListNode* tail = head;
        while(tail->next)
        {
            ListNode* newNext = tail->next->next;
            ListNode* newHead = tail->next;
            newHead->next = head;
            tail->next = newNext;
            head = newHead;
        }
        
        return head;
    }
};
