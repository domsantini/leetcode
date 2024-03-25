# Logic:
# Checking to see if all characters in a string occur the same amount of times
# Key thing to note here is that we can use multiple data structures and it's still O(n) times, dont be afraid of that
# When we populate the hashmap it's O(n) time and it's also O(n) time to convert to a set O(n + n) => O(2n) => O(n)

class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        map = defaultdict(int)

        for c in s:
            map[c] += 1
    
        # Convert our counts to a set and if they're all the same, there will only be one value in our set
        numSet = set(map.values())

        # Return if there's only one value
        return len(numSet) == 1