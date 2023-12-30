# Logic: Looking for the maxSum of a subarray. 
# BIG BOY. Basic implementation of Kadane's algorithm. Sliding window where you update based on previous values.
# In neetcodes explanation, given an array, you're basically taking the running sum, but if that running sum 
# becomes negative, you update your window to disregard all previous values that summed to negative, bc 
# next window wouldn't want to include that bc it couldn't possibly be the max sum

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Define our maxSum as arbitrary num, current sum to 0
        maxSum = nums[0]
        curSum = 0
        
        # Iterate through array
        for R in range(len(nums)):
            # Check if our current sum is negative and if so, reset
            if curSum < 0:
                curSum = 0
            
            # Add our next value to the current sum and update the maxSum
            curSum += nums[R]
            maxSum = max(maxSum, curSum)
        
        return maxSum