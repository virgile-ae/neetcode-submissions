# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        p_eq = root.val == p.val
        q_eq = root.val == q.val
        p_greater = root.val < p.val
        q_greater = root.val < q.val
        if p_eq or q_eq:
            return root
        elif p_greater and q_greater:
            return self.lowestCommonAncestor(root.right, p, q)
        elif p_greater or q_greater:
            return root
        else:
            return self.lowestCommonAncestor(root.left, p, q)

