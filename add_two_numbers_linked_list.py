'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
'''
# Definition for singly-linked list.
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def addTwoNumbers(self, L1, L2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        result = ListNode(0)
        result_tail = result
        
        while L1 or L2 or carry:
            val1 = L1.val if L1 else 0
            val2 = L2.val if L2 else 0
            carry, output = divmod(val1 + val2 + carry, 10)
            result_tail.next = ListNode(output)
            result_tail = result_tail.next
            
            L1 = L1.next if L1 else None
            L2 = L2.next if L2 else None
        
        return result.next
        
