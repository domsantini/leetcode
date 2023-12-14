# Logic:
# Looking for duplicate values, if we use a map, we can track nums and their instance
# If map does NOT contain num, then insert it, but if map does contain num then return bc that's a duplicate
# Then if we go through and don't return True, return False bc there would be no duplicates

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        map = {}

        for num in nums:
            if num not in map: 
                map[num] = 1
            else:
                return True
        return False
    
# Solution #2 (using hashset instead of hashmap)
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()

        for num in nums:
            if num in hashset: 
                return True
            hashset.add(num)
        return False