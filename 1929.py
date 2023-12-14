# Logic: 
# Want to return a concatenated array
# so we'll make a new away and iterate twice, appending each num in our OG array

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []

        for i in range(2):
             for num in nums:
                ans.append(num)

        return ans