# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return max(height(root.left) + height(root.right), self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right))
        
      

def height(root):
    if not root:
        return 0
    if not root.left and not root.right:
        return 1
    return 1 + max(height(root.right), height(root.left))
