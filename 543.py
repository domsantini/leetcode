# Logic: Looking to find the diameter of a given binary tree. That will equal the max height of the left and right sides.
# As always with tree problems, well use recursion to find the max height of either side

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # Set global variable. Using list bc lists are mutable (UNLIKE INTEGERS) and can be modified in functions and methods
        maxDiameter = [0]
    
        def height(root):
            # Step 1 - base case: If we reach leaf node, or empty node, the height will be 0
            if not root: 
                return 0
            # Determine the max height of left and right subtrees
            left = height(root.left) 
            right = height(root.right)
            # Update our maxDiameter variable, max of 0 / current diam, or left + right side of tree
            maxDiameter[0] = max(maxDiameter[0], left + right)
            
            # Return 1 + the max of left and right sides bc that will account for current node we are at
            return 1 + max(left, right)

        height(root)
        return maxDiameter[0]