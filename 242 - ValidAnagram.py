# 242. Valid Anagram 
# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

# Runtime 55 ms - Beats 42.71% | Memory 14.5 MB - Beats 58.66%

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # If the length of the strings are not equivalent, they cannot be anagrams so returns false immediately
        if len(s) != len(t):
            return False

        # Create a hashmap for both strings
        countS, countT = {}, {}
        
        # iterate through the hashmaps and at the key, which is the character of the string at the given index
        # up the count for each collision at that key
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)

        # itereate through the S hashmap keys and compare if the count of collisions at the given key is equal to
        # the collisions in the C hashmap, if not, it is not an anagram and return false
        for character in countS:
            if countS[character] != countT.get(character, 0):
                return False

        return True
