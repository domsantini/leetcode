# Logic:
# Grabbing the running sum, so each index is going to be the num at that index plus the previous mapped value
# BUT we can do this even better and in place, so we dont have to use extra memory to create a map, if we 
# use range(1, len(nums))

# Solution #1 (hashmap)
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ansMap = {}

        for i in range(len(nums)):
            ansMap[i] = nums[i] + ansMap.get(i - 1, 0)
        return list(ansMap.values())
    
# Solution #2 (in place)
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums)):
            nums[i] = nums[i-1] + nums[i]
        return nums
