# Logic: 
# Want to iterate through our list and find unique values. Two pointers, one to move through array, one to keep track of where to place next unique value.
# Starting at 2nd spot in array, compare if right pointer is equal to previous val, if they aren't equal, meaning unique val, replace nums[l] with nums[r]
# and increment left pointer, right pointer will increment itself in the loop

# Solution #1
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 1
        r = l

        for i in range(len(nums) - 1):
            if nums[i] == nums[r]:
                r += 1
            else: 
                nums[l] = nums[r]
                l += 1
                r += 1
        return l
    
    
# Solution #2 (use alternate loop)

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 1
        
        for r in range(1, len(nums)):
            if nums[r] != nums[r - 1]:
                nums[l] = nums[r]
                l += 1
        return l