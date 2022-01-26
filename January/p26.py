#1305. All Elements in Two Binary Search Trees
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1, root2):
        
        def inorder(root,ans):
            if root:
                inorder(root.left,ans)
                ans.append(root.val)
                inorder(root.right,ans)
            return ans
        
        l1 = inorder(root1,[])
        l2 = inorder(root2,[])
        l1.extend(l2)
        l1.sort()
        return l1