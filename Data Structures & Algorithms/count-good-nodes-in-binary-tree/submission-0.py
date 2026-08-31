# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        return self._goodNodes(root, root.val)

    def _goodNodes(self, root: Optional[TreeNode], current_max: int) -> int:
        if root is None:
            return 0

        new_max = max(current_max, root.val)
        left = self._goodNodes(root.left, new_max)
        right = self._goodNodes(root.right, new_max)

        res = left + right
        
        if root.val >= current_max:
            res += 1

        return res