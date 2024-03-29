# Logic:
# Find the longest subarray where the frequency of the nums is at most k, SO they could be under and it's valid
# ... wasn't reading the problem properly and got confused : / 

class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        # Define a default dict bc it makes incrementing a map easier
        countMap = defaultdict(int)
        # Define our left pointer and answer variable
        left = ans = 0

        # Define right and loop through nums
        for right in range(len(nums)):
            # For each number we encounter, incremement the frequency
            countMap[nums[right]] += 1

            # If we ever have an invalid case, where our frequency is larger than k, shrink the window until 
            # we are valid again, so we'll decrement whatever our left pointer value is and shift left up
            while countMap[nums[right]] > k:
                countMap[nums[left]] -= 1
                left += 1
            
            # As long as our window is valid, keep updating the ans
            ans = max(ans, right - left + 1)

        return ans