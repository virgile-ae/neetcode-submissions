# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if self.equalTrees(root, subRoot):
            return True

        if root is None:
            return False

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def equalTrees(self, left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:
        if left is None and right is None:
            return True

        if left is None or right is None:
            return False

        return left.val == right.val and self.equalTrees(left.left, right.left) and self.equalTrees(left.right, right.right)

