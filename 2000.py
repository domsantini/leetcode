# Logic:
# Given a string and a specific letter, swap the prefix of the string up until finding that letter

# Solution 1: 
class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        # Turn string into a list to work w/ swapping it easier
        word = list(word)
        left = 0
        
        for right in range(len(word)):
            # If we find our character enter swapping while loop
            if word[right] == ch:
                # Swap our pointers while they're not equal to each other
                while left < right: 
                    word[left], word[right] = word[right], word[left]
                    left += 1
                    right -= 1
                
                # Return the joined array
                return ''.join(word)

        # Return the rejoined string if we dont enter loop
        return ''.join(word)
    
# Solution 2 (faster on leet) w/ early return:
class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch not in word:
            return word
        
        word = list(word)
        left = 0

        for right in range(len(word)):
            if word[right] == ch:
                while left < right: 
                    word[left], word[right] = word[right], word[left]
                    left += 1
                    right -= 1

                return ''.join(word)
        