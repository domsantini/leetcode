# Logic: 
# Looking for missing number in an array. We're given an array of size n and the nums in that array are in the range [0, n] (n = 3, nums can be 0, 1, 2, 3)
# We can use a set here and looping through n + 1 values, check if the num is in the array, if not return the num

# Solution 1 (not great, n^2 in the worst case):
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # Define our set
        numSet = set()

        # Loop through nums and add to set
        for num in nums:
            numSet.add(num)

        # Loop through nums + 1 (nums is 0 indexed so if we have n = 3, then nums in the array will be 0, 1, 2, 3)
        for i in range(len(nums) + 1):
            # Return logic, if the num isnt in the set then it's missing
            if i not in numSet:
                return i

# Solution 2 (better time complexity bc only one loop, but making set does take time so maybe it's not better?):
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        numSet = set(nums)

        for i in range(len(nums) + 1):
            if i not in numSet:
                return i
