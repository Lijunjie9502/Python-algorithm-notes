# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from collections import defaultdict


class Solution:
    def deleteDuplication(self, pHead):
        if pHead is None: return None
        vals_dict = defaultdict(0)
        x = pHead
        while x is not None:
            vals_dict[x.val] += 1
            x = x.next
        x, y = pHead, None
        while x is not None:
            if vals_dict[x.val] > 1:
                if y is None:
                    pHead = x.next
                else:
                    y.next = x.next
            else:
                y = x
            x = x.next
        return pHead