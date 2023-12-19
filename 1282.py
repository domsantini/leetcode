# Logic: 
# We have an array of groupSizes and we're trying to order people in groups of their size. 
# A hashmap is perfect to track the size of the group and the people in that group size.
# Define a map and iterate through the array, adding the index for each size to the hashmap
# Run a check during the loop to see if the size of the group is full, if it is then .pop() 
# and put it into the answer array

class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        sizeMap = defaultdict(list)
        ans = []

        # For index, value in enumerate(groupSizes) -> returns both index and the value in the array
        for i, size in enumerate(groupSizes):
            sizeMap[size].append(i)

            if len(sizeMap[size]) == size:
                # sizeMap.pop(size) returns the array and removes it from the map then .append() adds it to the ans array
                ans.append(sizeMap.pop(size))
                
        return ans