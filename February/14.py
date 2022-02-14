# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#104. Maximum Depth of Binary Tree
class Solution:
    def maxDepth(self, root) -> int:
        
        if root is None:
            return 0
        
        leftans = self.maxDepth(root.left)
        rightans = self.maxDepth(root.right)
        
        return 1+ max(leftans,rightans)