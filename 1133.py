# Logic:
# We're looking for the largest number that occurs only once
# Make a map/dict to count the occurrences of each number then loop through the map and find the max

class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        numMap = defaultdict(int)
        ans = -1

        for num in nums:
            numMap[num] += 1
                
        # Need to specify map.items() to iterate                
        for key, value in numMap.items():
            if value == 1:
                ans = max(ans, key)

        return ans