# Logic:
# Looking to find the smallest subarray that sums to greater than or equal to the target
# Going to use a two pointer solution, which was pretty easy to whip up but one small caveat below made it slightly tricky

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # Define left pointer and tracker var for our sum. But trying to find the min, we can set our answer to a very large number
        # whatever solution we have will be lower and if not, we can check at the end if our ans is infinity and if so return 0 instead
        left, curr, ans = 0, 0, float('inf')

        # Define right pointer in our for loop
        for right in range(len(nums)):
            # Increment our current sum
            curr += nums[right]

            # While our current sum is greater than the target, update our ans for the length of the subarray, 
            # remove left most value from current sum and then increment our left pointer
            while curr >= target:
                ans = min(ans, right - left + 1)
                curr -= nums[left]
                left += 1
                
        # Finally perform the check if our ans is equal to infinity (this would be the case if we didnt find any valid subarrays),
        # and if it's not infinity just return our ans
        return 0 if ans == float('inf') else ans

