# Logic: 
# Comparing char counts in two different strings, ransom and magazine
# If the ransom string can be made from the chars in magazine, then return true

# Solution 1:
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # If there are less characters in mag than ransom, can't make the string and early return
        if len(magazine) < len(ransomNote):
            return False

        # Tried messing w/ the counter object and it does make things easier, idk the impact on time / memory complexity though
        ransomChar = Counter(list(ransomNote))
        magChar = Counter(list(magazine))

        
        for key in ransomChar.keys():
            # If our ransom char isn't in the magazine characters, OR if the magazine char count is less than the ransom, return false
            if key not in magChar.keys() or magChar[key] < ransomChar[key]:
                return False

        return True
    
# Solution 2 (try using just one hashmap 👀)