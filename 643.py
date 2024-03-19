# Logic: 
# Looking to grab the maximum average subarray w/ a fixed window size 
# BUT bc everything will be divided by k, we can just find the maximum numerator

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        curr = 0

        # Iterate through first window and get the current sum
        for i in range(k):
            curr += nums[i]
        # Update our answer for our current sum
        ans = curr

        # Loop through remainder of array
        for i in range(k, len(nums)):
            # Add next element, remove first element
            curr += nums[i] - nums[i - k]
            ans = max(curr, ans)

        # Return the max average, so current max sum divided by k  
        return ans / k