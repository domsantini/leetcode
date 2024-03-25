# Logic: 
# Reversing the string, but only alpha chars. Was making this WAY harder than I needed, but using .isalpha() it's ez pz
# Loop through using two pointers and if the both pointers are alpha, swap them

class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        s = list(s)
        left, right = 0, len(s) - 1

        while left < right: 
            if not s[left].isalpha():
                left += 1
            elif not s[right].isalpha():
                right -= 1
            else: 
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1

        return ''.join(s)