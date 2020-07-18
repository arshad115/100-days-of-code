# -------------------------------------------------------
# Add Two Numbers - https://leetcode.com/problems/add-two-numbers/
# -------------------------------------------------------
# Author: Arshad Mehmood
# Github: https://github.com/arshad115
# Blog: https://arshadmehmood.com
# LinkedIn: https://www.linkedin.com/in/arshadmehmood115
# Date : 2020-07-18
# Project: 100-days-of-leetcode
# -------------------------------------------------------

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            return l2
        elif l2 is None:
            return l1

        carry = 0
        a = l1
        b = l2

        resultList = ListNode()
        current = resultList

        while (a != None or b != None):
            x = a.val if a else 0
            y = b.val if b else 0

            sum = x + y + carry

            result = sum % 10
            carry = int(sum / 10)

            node = ListNode(result)

            current.next = node
            current = node

            a = a.next if a else None
            b = b.next if b else None

        if carry > 0:
            current.next = ListNode(carry)

        return resultList.next


l1 = ListNode(2)
l11 = ListNode(4)
l1.next= l11
l12 = ListNode(3)
l11.next = l12

l2 = ListNode(5)
l21 = ListNode(6)
l2.next= l21
l22 = ListNode(4)
l21.next = l22

# Numbers are stored in reverse order so carry goes to the right

solution = Solution()
list = solution.addTwoNumbers(l1,l2)
print(list)