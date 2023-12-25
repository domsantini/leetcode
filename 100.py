# Logic: Given two trees, determine if the trees are the same. Tree traversal lends itself well to recursion.
# Recursion has two steps:
#   Step 1: Identify base case (when you exit loop)
#   Our base case here is when there are two empty trees, one tree is empty and the other isn't or if the value isn't the same
#   Step 2: Call the function with a different input (smaller slice of the function)
#   Here we'd be calling our function with the left and right nodes of the tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Step 1: Identifying base case and returning if satisfied
        if not p and not q: 
            return True
        if not p or not q or p.val != q.val:
            return False
        
        # Step 2: Calling function with smaller inputs, individual nodes in this case
        return (
            self.isSameTree(p.left, q.left) # Call w/ left pointers, runs through checks returns True if satisfied
            and self.isSameTree(p.right, q.right) # Call w/ right pointers, run through checks returns True if satisfied
        )