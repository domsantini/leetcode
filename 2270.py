# Logic:
# First prefix sum problem. Prefix sum is a technique to precompute sums of our array so look up is O(1) in the future
# Start by building prefix by adding newest item in num array to last element of prefix sum
# Next we go through and calculate our sums of the subarrays (always going to be end of subarray, minus the beginning bit to our subarray which is easy to find w/ prefix sum array)

class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        # Build prefix sum array by starting w/ first item in nums array
        pre = [nums[0]]
        for i in range(1, len(nums)):
            # Starting at index 1, add next num value (nums[1], nums[2], nums[3], etc until end) to the last prefix value pre[len(pre) - 1] (at start len(pre) is 1 so 1 - 1 would be 0, which is current last item in prefix sum)
            pre.append(nums[i] + pre[len(pre) - 1])

        # Declare our answer or count of valid splits (valid if left side is > than right side)
        ans = 0
        
        # Iterate through valid split options (-1 bc you can't split on last element of nums)
        for i in range(len(nums) - 1):
            # Left side of the split will always be our index of prefix sum
            left = pre[i]
            # Right side of split will always be last element of prefix sum - left side
            right = pre[-1] - pre[i]
            # If valid add to ans
            if left >= right:
                ans += 1
        
        return ans 