# Logic:
# Reversing string but maintaining the word order and the space characters
# Thing to remember here are edge cases, we have ifs nested in "if or" statements

class Solution:
    def reverseWords(self, s: str) -> str:
        # Convert s to list so that we can work w/ it easier
        s = list(s)
        # Initialize left pointer at start and initialize right pointer below in for loop
        left = 0

        for right in range(len(s)):
            # Set conditions for when to perform swap, if we find space char or if right pointer is last element in string / array
            # right == len(s) - 1 bc for loops indexing and starts at 0 so last element is at length of array - 1
            if s[right] == ' ' or right == len(s) - 1:
                # This is new, using temp pointers bc right is keeping track of where we are in the array
                temp_left, temp_right = left, right - 1 

                # Here's what I'm talking about in the logic, we want to set our pointers differently depending on if were at the 
                # end of the array or is were at a space char
                if right == len(s) - 1:
                    temp_right = right
                
                # Normal while loop for two pointers, while theyre not crossing perform our swap
                while temp_right > temp_left:
                    # Swap chars and update pointers
                    s[temp_right], s[temp_left] = s[temp_left], s[temp_right]
                    temp_right -= 1
                    temp_left += 1
                
                # Once we've swapped, update our left pointer to the char after the space
                left = right + 1
                
        return ''.join(s)