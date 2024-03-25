# Logic:
# Want to find the nums that occur in each of our arrays. Bc we're counting, we want to use a hashmap (defaultdict bc it allows us to specify a default value)
# So we'll define our map/defaultdict, we'll loop through the arrays in nums, and then each num in each array
# we're going to update the count for that given number and check if the count is equal to the length of our og number array
# and if so, we'll add that number to our ans array. We do this check bc an answer will only be valid if it's present in each array, so if freq == len(nums)

class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        map = defaultdict(int)
        ans = []

        for array in nums:
            for num in array:
                map[num] += 1

                if map[num] == len(nums):
                    ans.append(num)

        # Return sorted array bc the problem asks for it
        return sorted(ans)