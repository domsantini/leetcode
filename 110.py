# Logic: Determining if tree is height balanced (the height of any given nodes left and right side <= 1)
# For time complexity, we'll do dfs so that we only need to visit each node once.
# Tricky bit is that you need to track the balanced status as you go, as well as the max heights of given node
# Implement a solution that tracks two return values [balanced, heightOfTree]

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def getHeight(root):
            # Base case if we reach an empty node, height is 0 and left / right pointers would be null so that would be balanced True
            if not root:
                return [True, 0]
            
            # Recursively get the height of the left and right trees
            left, right = getHeight(root.left), getHeight(root.right)
            
            # Determining balanced status, if subtrees are True and then if diff of max left and right are <= 1
            balanced = (
                left[0] and right[0] and
                abs(left[1] - right[1]) <= 1
            )
            
            # Returning the balanced status and then maxHeight of tree
            return [balanced, 1 + max(left[1], right[1])]
        
        # Calling our function and returning boolean balanced var
        return getHeight(root)[0]