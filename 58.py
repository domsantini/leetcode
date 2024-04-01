# Logic: 
# We're given a string and we need to find the length of the last word. BUT there are spaces.. what do??
# Just split it bc .split() wont contain spaces/ whitespace. Codes pretty straight forward. 

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        return len(s.split()[-1])