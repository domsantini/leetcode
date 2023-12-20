# Logic:
# Looping through strings and finding palendromes, trick here is to use left pointers to avoid brute force solution.
# Remember to use while left <= right and use the pointers w/in the string 
# Tricky is to use the right methods to trim the string of non alnum characters, but REMEMBER EARLY RETURNS

class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1

        while left <= right:
            if not s[left].isalnum():
                left += 1
                continue
            if not s[right].isalnum():
                right -= 1
                continue
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True