# Logic:
# Looking for longest subarray with less than k 0s, simple.
# When we hit > k 0s, reset our window

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = curr = ans = 0

        for right in range(len(nums)):
            # Got caught up on my ifs bc I had them as "0", but I'm looking at an array
            if nums[right] == 0:
                curr += 1
            while curr > k:
                if nums[left] == 0:
                    curr -= 1
                left += 1
            ans = max(ans, right - left + 1)

        return ans