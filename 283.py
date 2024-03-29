# Logic: 
# Moving all 0 values to the end of our array. Bc we want to keep the relative order of non-zeros, 
# look for non-zeros instead and anytime our right pointer doesn't equal 0, swap w/ the left

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        left = 0

        for right in range(len(nums)):
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                