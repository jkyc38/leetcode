"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

"""
from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        #find the shortest string then loop through that string character by character with each word in the strs
        if not strs:
            return ""
        
        short = strs[0]
        #get the shortest string
        for s in strs:
            if len(s)< len(short):
                short = s

        for i in range(len(short)):
            char = short[i] # this gets the current character
            for word in strs: #loops through each word with the respective index and checks if it matches with the current char
                #if it doesn't match then you return the string up until the current index
                if word[i]!=char:
                    return short[:i]

        return short

        