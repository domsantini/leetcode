# Logic:
# Going to be looking for the difference between our target and number in nums array. Bc the difference can only yield one solution, 
# we'll eventually run into our difference at some point in the array.
# Mapping through our array, if the difference isn't in our map, we add the number and it's associated index. 
# If the difference IS in the array, we return the index of map item (map[diff]) bc diff exists in
# our map already, so map[diff] will be equal to the index, so we return map[diff] and i, which will be the index of the current value

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        
        for i in range(len(nums)):
            diff = target - nums[i]

            if diff not in map:
                map[nums[i]] = i
            else:
                return [map[diff], i]