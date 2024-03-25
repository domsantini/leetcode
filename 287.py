# Logic:
# Looking for duplicate numbers. Loop through our nums array and if current num is in the set, return the number
# otherwise add it to the st

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        numSet = set()

        for num in nums:
            if num in numSet:
                return num
            else:
                numSet.add(num)