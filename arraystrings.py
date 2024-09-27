class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = "aeiouAEIOU"
        s = s.lower()
        contained_vowels = ""
        for c in s:
            if c in vowels:
                contained_vowels+=c
        
        pointer = len(contained_vowels)-1

        rev = ""

        for c in s:
            if c in contained_vowels:
                rev+=contained_vowels[pointer]
                pointer-=1
                continue
            rev+=c
        return rev
        


'''
TEST CASE
Input: s = "hello"
Output: "holle"

Input: s = "leetcode"
Output: "leotcede"
'''