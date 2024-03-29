# Logic: 
# Given a list of matches we want to return two arrays, one of players w/ 0 losses and one of players w/ 1 loss
# I got tripped up on the intuition here and was focusing on wins, which didn't really matter

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        lossMap = defaultdict(int)
        ans = [[],[]]

        # This is how you loop over the [winner, loser] for each match
        for winner, loser in matches:
            # If they're winner, add 0 to their losses, if they're loser add 1 to their losses
            lossMap[winner] += 0
            lossMap[loser] += 1

        # Loop through the map, sorted bc question asks for it, and if they have zero losses add to first array of ans
        # If they have 1 loss, add to 2nd array of ans
        # This is also a good way to loop through the map w/ just the key, bc we can access the value w/ map[key] syntax
        for player in sorted(lossMap.keys()):
            if lossMap[player] == 0:
                ans[0].append(player)
            elif lossMap[player] == 1:
                ans[1].append(player)

        return ans