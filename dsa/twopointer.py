def validPalindrome(s:str) -> bool:
    alnum = ''
    valid = True
    for char in s:
        if char.isalnum():
            alnum+=char
    
    s = alnum.lower()
    start = 0
    end = len(s)-1
    for i in s:
        if s[start] != s[end]:
            valid = False
            break
        else: 
            valid = True
        start+=1
        end-=1

    return valid
    
# s = "Was it a car or a cat I saw?"
# s = "tab a cat"
# valid = validPalindrome(s)
# print(valid)


def removeElement():

    pass

from collections import Counter

def checkInclusion(s1, s2) -> bool:
    #initialize hashmap between two pointers

    perms = Counter(s1)

    l, r = 0,0
    #sequentially check that the right pointer fulfills the condition that the letter is in the set if it is then 
    while r< len(s2):

        if s2[r] not in perms:
            r+=1
        
        pass 
    pass

s1 = "hello"
# perms = {}
# for c in s1:
#     if c in perms:
#         count = perms[c]
#         count+=1
#         print(count)
#         perms[c] = count
#         continue
#     perms[c] = 1
 
perms = Counter(s1)
print(perms)
print(perms['h'])

l, r = 0, 3

print(s1[l:r])