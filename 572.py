# Logic: Going through a tree and finding if the tree contains a given subtree. Tree problem, so you know it's that recursion.
# BUT theres a little more here. Looking at the problem, need to check if the subtree exists and also if it does, you need to 
# check if the subtree is the same. BIG LIGHTBULB MOMENT. YOU CAN WRITE HELPER FUNCTIONS.
# Step 1 here then is to write helper function sameTree(root, subRoot)
#   And bc you're doing recursion there look for edge cases in comparing two trees
#   If the trees are both empty, you can continue to comparison logic, if comparison logic doesn't execute, return False
#
# Now that you have helper function written, two steps for main problem
# Step 1: Edge cases for is the subRoot a subtree
#   If the subRoot is empty, then it'll always be a subtree -> return True
#   If the subRoot is NON-empty, but root is empty -> return False
#   If neither of those execute, you'll want to check if your current nodes are the same tree, so call your sameTree() function
#   FINALLY, if that doesn't execute you can check recursively if the left or right side of the root is subtree and the same 


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # Step 1: Find edge cases of main problem
        # If the subRoot is empty it'll be a subtree no matter what
        if not subRoot: 
            return True
        # If we have a subRoot, but the root is null, false, can't be subtree
        if not root: # Order of conditions matter here, bc this wont execute
                     # if there is a subRoot, bc if there isn't the above condition
                     # will execute first 
            return False
        # So if we have trees, check w/ helper if they're the same, if so gooch
        # and return 
        if self.isSameTree(root, subRoot):
            return True
        # Finally, if we get through all edge cases check and still nothing, 
        # check if the subRoot is subtree of either left or right node
        return (
            self.isSubtree(root.left, subRoot) or
            self.isSubtree(root.right, subRoot)
        )
        

    # Define a helper function to compare if the trees are the same
    def isSameTree(self, root, subRoot):
        # Step 1: Find edge cases
        # If both trees are empty
        if not root and not subRoot:
            return True
        # If neither tree is empty and the values are the same
        if root and subRoot and root.val == subRoot.val:
            # Step 2: Recursive calls
            # If the left and right right pointers of the tree are also the same
            return (
                self.isSameTree(root.left, subRoot.left) and
                self.isSameTree(root.right, subRoot.right)
            )
        # If neither of the two above conditions execute this would mean one tree
        # is empty while the other is non-empty and then they aren't the same tree
        return False


        


        
        
