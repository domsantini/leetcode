# Logic: 
# Pretty straight forward when I actually read the question.. oof. 

class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        ans = []

        for i in range(len(nums)):
            ans.append(nums[nums[i]])
        return ans