# Logic:
# Made this problem way harder than it needed to be. Just swapping characters in string s to t, but it costs the 
# absolute value diff between s[i] and t[i]
# All we need to do is loop through w/ a sliding window and once the budget goes below 0, add back in our left pointer diff and increment left

class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        left = ans = 0

        for right in range(len(s)):
            maxCost -= abs(ord(s[right]) - ord(t[right]))

            if maxCost < 0:
                maxCost += abs(ord(s[left]) - ord(t[left]))
                left += 1

            ans = max(ans, right - left + 1)

        return ans