# Logic: Finding the longest path in a tree. Traversing tree is great for recursion.
# Recursion has two steps:
#   Step 1: Identify base case (when you exit loop)
#   Our base case here would be if we find an empty node, in that case we'd return 0
#   Step 2: Call the function with a different input (smaller slice of the function)
#   We're looking for the longest path, so we'll call the max function on our left and right nodes
#   and add 1 to each bc that'd denote that we have a node

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Step 1: Identify base case if we dont have a node, you'd return 0
        if not root:
            return 0
        # Step 2: Make our recursive call, finding the max between our left and right nodes
        return (
            max(1 + self.maxDepth(root.left), 1 + self.maxDepth(root.right))
        )