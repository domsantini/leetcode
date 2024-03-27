# Logic:
# Given a string of text, find the amount of times we can spell the word 'balloon' w/ the characters
# How to think of this one is what's the minimum potential times we can spell 'balloon' given our characters

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        map = {
            'b': 0,
            'a': 0,
            'l': 0,
            'o': 0,
            'n': 0
        }

        for c in text:
            if c not in ['b', 'a', 'l', 'o', 'n']:
                continue
            map[c] += 1

        potential = 1000000 

        for key in map:
            if key in ['b', 'a', 'n']:
                potential = min(potential, map[key])
            else:
                potential = min(potential, map[key] // 2)

        return potential