# Logic:
# We're counting elements in our array that are equal to x + 1, so in array of [1, 2, 3], 1+1 = 2 and 2+1 = 3, so two such items are in our array
# We make a set and loop through w/ our condition, incrementing our ans variable if the conditions true

class Solution:
    def countElements(self, arr: List[int]) -> int:
        numSet = (arr)
        ans = 0

        for num in arr:
            if num + 1 in numSet:
                ans += 1
        
        return ans