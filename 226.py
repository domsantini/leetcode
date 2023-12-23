# Logic: This is a tricky one. We're solving this using recursion and it's hurting my brain.
# We need to find a sub problem, which in this case is to find a root and swap it's left and right nodes.
# For recursion we also need a base case, which is when we tell our recursion to stop. In the factorial 
# example it was when our number is 1, bc the factoral function is !n = n * (n-1) ... 1, so once we get to 1, 
# exit the loop. 
# Here it's once 

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        # Step 1. Find the base case, in this problem it would be if our root doesn't have
        # a left or right pointer. Checking "if not root" is a way to check if the root
        # evaluates to false, which would be true if it doesn't have any left or right pointers
        if not root:
            return root

        # If we do have a root node, call the function to invert the node on the left
        # and right nodes
        self.invertTree(root.left)
        self.invertTree(root.right)

        root.right, root.left = root.left, root.right

        return root