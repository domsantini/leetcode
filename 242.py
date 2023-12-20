# Logic: 
# Need to see if two words are anagrams (all letters present in both words in same quantity)

# Solution #1 EZ

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)

    
# Solution #2 using hashmap
    
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Early return if the strings aren't same length. Nice edge case hedging here.
        if len(s) != len(t):
            return False
        
        # Create maps
        mapS, mapT = {}, {}
        
        # For each character in the strings, increment it by 1, or if it's not there add it by getting 0
        for i in range(len(s)):
            mapS[s[i]] = 1 + mapS.get(s[i], 0)
            mapT[t[i]] = 1 + mapT.get(t[i], 0)
        
        # "for c in map" gives you the indexes, so check if the indexes match and early return if not
        for c in mapS:
            if mapS[c] != mapT.get(c, 0):
                return False
        
        return True
    
# Solution #3 using hashmap AND QUICK
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Get that nice, early return in
        if len(s) != len(t):
            return False

        # Define like this so that we have default values
        mapS, mapT = defaultdict(int), defaultdict(int)

        # Add our values
        for i in range(len(s)):
            mapS[s[i]] += 1
            mapT[t[i]] += 1
        
        # Nice and easy return
        return mapS == mapT