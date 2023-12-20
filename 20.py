# Logic:
# Basically we can't have an ending paren w/o it closing out a paren. We just run a bunch of else conditions here. 
# I think I did this pretty weak and theres a better way.

class Solution:
    def isValid(self, s: str) -> bool:
        opened = []

        for char in s:
            if char in ['(','[','{']:
                opened.append(char)
            else:
                if not opened \
                or (char == ')' and opened[-1] != '(') \
                or (char == ']' and opened[-1] != '[') \
                or (char == '}' and opened[-1] != '{'):
                    return False    
                else:
                    opened.pop()
        return not opened

        