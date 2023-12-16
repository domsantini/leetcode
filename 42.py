# Logic:
# We're looking to group anagrams here so we're going to use a map of some sort, but a typical map will give us a KeyError if we try to add a value to a key that doesn't exist.
# For that reason we're going to use a defaultdict(list) w/ list as default, so that when we add a new value to a key, if it doesn't exist it will create an empty list for us to add to.
# Once we define our map, we iterate through our list of strs, and for each word we sort the word to use as our key (all anagrams will have same sorted key)
# sorted() will turn our word into a list, so we ''.join, so join the list into a string.
# Using the sorted word as our key we append each word in the list and finally return the values of the map as a list

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Create a defaultdict(list) so that if we run into new values, it'll create an empty list as value and not return a KeyError
        map = defaultdict(list)

        # Loop through each word in strs array
        for word in strs:
            # Sort the word so that we can use the sorted_word as map key
            sorted_word = ''.join(sorted(word))
            # Using sorted_word as key, append the word as value
            map[sorted_word].append(word)
        
        # Return the list of values from map
        return list(map.values())
