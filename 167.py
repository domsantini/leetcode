# Logic: Finding two int sum that matches target.
# We have sorted array so we can use two pointers to iterate through in one pass.
# If the sum > target shift right pointer down, if the sum < target shift left pointer down

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        
        while left < right:
            if numbers[left] + numbers[right] > target:
                right -= 1
            elif numbers[left] + numbers[right] < target:
                left += 1
            else: 
                return [left+1, right+1]