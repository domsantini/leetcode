# Logic:
# We want to find the longest string w/ unique characters
# Make a map of characters and any time the count of a char is greater than 1, slide our window and thus decrement the char

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        numMap = defaultdict(int)
        left = ans = 0

        for right in range(len(s)):
            numMap[s[right]] += 1

            while numMap[s[right]] > 1:
                numMap[s[left]] -= 1
                left += 1
            
            ans = max(ans, right - left + 1)

        return ans