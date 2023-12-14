# Logic: 
# Want to use a pointer to track where we are replacing val. If nums[i] did equal val, we continue forward looking for a number to replace it w/.
# If nums[i] does NOT equal val, then we want to replace nums[k] (last val num) with nums[i]

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
    
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k
    
