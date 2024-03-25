# Logic:
# We want to see if a sentence contains all letters of alphabet. We can just loop through string and add characters to set
# and if our set length is 26 characters long, then it contains each letter. Otherwise it doesn't

class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        letters = set()

        for c in sentence:
            letters.add(c)

        return len(letters) == 26