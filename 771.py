# Logic:
# Similar to ransom note, given a jewel and stone string, looking to see how many times the characters from jewel appear in stones

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        ans = 0
        stonesMap = defaultdict(int)

        for c in stones:
            stonesMap[c] += 1

        for c in jewels:
            ans += stonesMap[c]

        return ans
