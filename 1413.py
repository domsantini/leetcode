# Logic:
# This was a bit tricky to understand at first, but we're trying to find the minimum value that when added to our prefix sum, the total will be > 0. 
# So if our minimum value in prefix sum was -4, then the answer would be 5, bc that's the smallest number when added to -4, that would give us 1, or > 0
# Little bit tough to understand the wording of the problem, but the hint helped
# Oh, and this can be done in place bc we dont need nums array, but set up the prefix sum to start for practice

class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        prefix = [nums[0]]
        for i in range(1, len(nums)):
            prefix.append(nums[i] + prefix[len(prefix) - 1])

        # Set ans to 1 bc it had to be positive number, or non 0
        ans = 1

        for i in range(len(prefix)):
            ans = min(ans, prefix[i])
        
        # This was a little bit of new syntax to get rid of an if condition at the end here
        # Return (thing to return) if (condition) else (other thing to return)
        return ans if ans > 0 else abs(ans) + 1
            
