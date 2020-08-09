# https://leetcode.com/problems/merge-two-sorted-lists
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = current = ListNode(0)
        while l1 != None and l2 != None:
            temp1 = l1
            temp2 = l2
            ct = 0
            n = None
            if l1.val <= l2.val:
                n = l1
                l1 = l1.next
            else:
                n = l2
                l2 = l2.next
            current.next = n
            current = current.next
        if l1 != None:
            current.next = l1
        if l2 != None:
            current.next = l2
        return head.next
