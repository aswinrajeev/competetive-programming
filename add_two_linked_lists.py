"""
Add Two Numbers
===============

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, 
 and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example 1:
==========
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Example 2:
==========
Input: l1 = [0], l2 = [0]
Output: [0]

Example 3:
==========
Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        carry = 0
        l1_current = l1
        l2_current = l2

        l3_previous = None
        l3 = []

        while l1_current or l2_current:
            sum = (
                (l1_current.val if l1_current is not None else 0)
                + (l2_current.val if l2_current is not None else 0)
                + carry
            )
            lsd = sum % 10
            carry = 1 if sum > 9 else 0

            l3_current = ListNode(lsd)

            if l3_previous:
                l3_previous.next = l3_current

            l3_previous = l3_current
            l3.append(l3_current)

            l1_current = l1_current.next if l1_current and l1_current.next else None
            l2_current = l2_current.next if l2_current and l2_current.next else None

        if carry and l3_previous:
            l3_current = ListNode(carry)
            l3_previous.next = l3_current

        return l3[0] if len(l3) > 0 else None
