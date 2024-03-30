# Logic: 
# Given a string and a size k, we're looking for the maximum number of vowels in the substring of size k
# Use a sliding window of fixed size approach

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        # Define vowels
        vowels = ['a','e','i','o','u']
        # Define our left pointer and variable to track current number of vowels in a string
        left = curr = 0
    
        # Loop through our first window and get the starting num of vowels
        for i in range(k): 
            if s[i] in vowels:
                curr += 1  

        ans = curr

        # Loop through rest of the string, incrementing if s[right] is a vowels and decrementing curr if s[left] is a vowel, 
        # Shift our left pointer no matter what
        for right in range(k, len(s)):
            if s[right] in vowels:
                curr += 1
            if s[left] in vowels:
                curr -= 1
            left += 1
            
            # Update our answer to the max value of current vowels and ans
            ans = max(ans, curr)

        return ans