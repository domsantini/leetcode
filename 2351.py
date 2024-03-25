# Logic:
# Looking for first repeated character in a string
# We can use a set here, bc we dont need to know frequency of characters, just if a number has appeared already

class Solution:
    def repeatedCharacter(self, s: str) -> str:
        # Declare set. Can't have set be the variable name, so sett or seen or something like that
        sett = set()
        
        # Loop through the chars in string and if it exists then it's been seen before, return it
        for c in s:
            if c in sett:
                return c
            # If it hasn't been seen before add it
            else:
                sett.add(c)
