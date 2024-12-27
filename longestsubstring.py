class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashset = set() #init hash table to track all the seen chars
        # use sliding window
        # sliding window conditions
        # use set to track all seen chars
        # if char is in set then u increment the left pointer and remove the char in the set
        # use something to update the count
        l, r = 0, 0
        max_length = 0 #used to track length of longest substring

        for r in range(len(s)):
            # if i find a duplicate then i remove it from the set and increment the left pointer
            while s[r] in hashset:
                hashset.remove(s[l])
                l+=1
            #add every char into the set
            hashset.add(s[r])
            #calculates the length of substring via the length of the set and the current length of substring
            max_length = max(max_length, len(hashset))
        
        return max_length

