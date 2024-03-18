# Logic: 
# Looking to sort squared numbers in increasing order given a non-decreasing array. Can use two pointers and work towards middle
# given the absolute value is what were adding to list. So biggest number will be on either most bound. Comparing and working in 
# we add the biggest num to our ans array, and return it reversed by using slicing syntax ans[::-1]

def sortedSquares(self, nums: List[int]) -> List[int]:
        ans = []
        left = 0
        right = len(nums) - 1


        while left <= right: 
            if nums[left] * nums[left] > nums[right] * nums[right]:
                ans.append(nums[left] * nums[left])
                left += 1

            else:
                ans.append(nums[right] * nums[right])
                right -= 1

        return ans[::-1]
