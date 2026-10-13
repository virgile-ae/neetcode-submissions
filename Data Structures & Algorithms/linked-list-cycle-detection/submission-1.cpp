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
    bool hasCycle(ListNode* head) {
        if (head == nullptr) return false;

        ListNode* left{head};
        ListNode* right{head->next};

        while (left != nullptr && right != nullptr) {
            if (left == right) return true;

            left = left->next;

            right = right->next;
            
            if (right == nullptr) return false;

            right = right->next;
        }

        return false;
    }
};
