# -------------------------------------------------------
# Remove Nth Node From End of List - https://leetcode.com/problems/remove-nth-node-from-end-of-list/
# -------------------------------------------------------
# Author: Arshad Mehmood
# Github: https://github.com/arshad115
# Blog: https://arshadmehmood.com
# LinkedIn: https://www.linkedin.com/in/arshadmehmood115
# Date : 2020-07-23
# Project: 100-days-of-leetcode
# -------------------------------------------------------
import sys
from math import inf
from statistics import median
from typing import List
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:

        length = 0
        node = head
        while node != None:
            node = node.next
            length +=1

        node = head
        prev = None
        step = 0

        remove = length - n + 1
        while node != None:
            step += 1

            if step == remove and step == 1:
                head = node.next
            elif step == remove:
                prev.next = node.next
            else:
                prev = node
                node = node.next

        return head


l1 = ListNode(1)
l11 = ListNode(2)
l1.next = l11
l12 = ListNode(3)
l11.next = l12

l2 = ListNode(4)
l12.next = l2
l21 = ListNode(5)
l2.next = l21

n = 5

solution = Solution()
linkedList  = solution.removeNthFromEnd(l1, n)

node = linkedList
while node != None:
    print(node.val)
    node = node.next