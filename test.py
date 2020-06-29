# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None: return []
        stacks = [deque(), deque()]
        current_stack, next_stack = 0, 1
        res, res_level = [], []

        stacks[current_stack].append(root)
        while stacks[0] or stacks[1]:
            item = stacks[current_stack].pop()
            res_level.append(item.val)
            if current_stack == 0:
                if item.left is not None: stacks[next_stack].append(item.left)
                if item.right is not None: stacks[next_stack].append(item.right)
            else:
                if item.right is not None: stacks[next_stack].append(item.right)
                if item.left is not None: stacks[next_stack].append(item.left)
            if not stacks[current_stack]:
                current_stack, next_stack = next_stack, current_stack
                res.append(res_level)
                res_level = []
        return res
                

                