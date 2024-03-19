# Logic:
# Sliding window looking for number of subarrays (can use len of array trick)

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        # Do this here bc our while loop would always be true (curr starts at 1, k would be 1)
        if k <= 1: 
            return 0
        
        # Initialize variables but curr = 1 bc were doing multiplication
        left = ans = 0
        curr = 1
        
        for right in range(len(nums)):
            # Update current to sum of window
            curr *= nums[right]
            # When invalid 
            while curr >= k:
                # Shrink window by removing left most from product
                curr /= nums[left]
                # Increment window
                left += 1

            # Add current length of array to ans
            ans += right - left + 1

        return ans
