# Logic: 
# Want to find number of subarrays that have an equal number of odd values to k (k = 3, we want subarrays w/ 3 odd values)
# Detailed explanation below, but we basically want to find prefix sums that are equal to prefixSum - k. Any prefix sum equal
# to prefixSum - k is a valid subarray of our condition

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:        
        # Neat trick to discern easily between even and odd numbers, replace evens w/ 0 and odd w/ 1
        # so you can do a simple count 
        for i in range(len(nums)):
            nums[i] = 0 if nums[i] % 2 == 0 else 1

        # Define our count map/dict
        counts = defaultdict(int)
        # Initialize { 0: 1 } bc an empty subarray sum is 0, so that occurs once
        counts[0] = 1
        # Intialize curr (which will track prefix sum) and ans variable
        curr = ans = 0

        # For each num in nums (new nums w/ only 0s and 1s) we want to update our prefix sum 
        # IF our prefix sum minus k value is in our count map, that is a valid subarray for our condition
        # Example: If k = 3 (were looking for subarrays with 3 odds), then any subarray sum of 3 is valid
        # In our first example, we eventually have curr = 3, and so we have curr - k => 3 - 3 => 0
        # Our map[0] is 1, so at this point theres 1 valid subarray that fits our condition, so we add that 
        # value to our ans 
        # And finally we add the prefix sum value to our map, bc if we run into a curr - k that equals our prefix 
        # we want to add that value to our ans
        for num in nums:
            curr += num
            ans += counts[curr - k]
            counts[curr] += 1
            
        return ans

