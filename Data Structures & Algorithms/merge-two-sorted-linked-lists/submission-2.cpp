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
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        if (list1 == nullptr) return list2;
        if (list2 == nullptr) return list1;

        ListNode *newList;

        if (list1->val < list2->val) {
            newList = list1;
            list1 = list1->next;
        } else {
            newList = list2;
            list2 = list2->next;
        }

        ListNode *head{newList};

        while (list1 != nullptr && list2 != nullptr) {
            if (list1->val < list2->val) {
                newList->next = list1;
                newList = newList->next;
                list1 = list1->next;
            } else {
                newList->next = list2;
                newList = newList->next;
                list2 = list2->next;
            }
        }

        newList->next = list1 != nullptr ? list1 : list2;

        return head;
    }
};
