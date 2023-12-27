# Logic: Decoding a message, so we'll need to make a keyMap from our key and then iterate through the word
# This first solution is pretty poor, so need to do this a bit quicker

# Solution #1:
class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        keyMap = {}
        i = 97
        ans = ''

        for k in key.replace(' ',''):
            if k not in keyMap:
                keyMap[k] = chr(i)
                i += 1

        for m in message:
            if m == ' ':
                ans += ' '
            else:
                ans += keyMap[m]
        return ans
    
# Solution #2:
class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        # Defining keyMap w/ space char
        keyMap = {' ': ' '}
        # Defining i = 97 to use below to map key to a-z
        i = 97

        for k in key:
            # Condition here to get 26 chars defined by problem, skipping duplicates and spaces
            if k not in keyMap and k != ' ':
                # Set keyMap of key char to the letter of alphabet, iterating once you input letter
                keyMap[k] = chr(i)
                i += 1
        # Nice little trick here, return the string '', joining based on our map but iterating through chars in message
        return ''.join(keyMap[m] for m in message)