# Logic: Replacing duplicates, but there can be at least 2 of each number
# Method is going to be to check for streaks of numbers and replace at most 2 numbers

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Need two pointers to track current number and where we will be replacing duplicate values
        # Define both at start of array
        l, r = 0, 0

        # To ensure one pass, while loop
        while r < len(nums):
            # Method we'll use is keeping track of current string of nums
            # When we get to a new num, do i number of replacements where 
            # i is the minimum of 2, or the current count of streak
            count = 1
            # Check if our pointer index is in bounds and if we're on streak, 
            # so if nums[r] and nums[r + 1] are the same number
            while r + 1 < len(nums) and nums[r] == nums[r + 1]:
                # While above conditions true, increment our count and shift pointer
                count += 1
                r += 1
            
            # Once we break from that condition / once we find new number, do i replacements
            for i in range(min(2, count)):
                # Do replacement and shift left pointer
                nums[l] = nums[r]
                l += 1
            # We ended at last number in streak, so shift right pointer to new number and 
            # reset streak counter condition
            r += 1
        # Return the L pointer, which will be last index of array / number of items in array
        return l