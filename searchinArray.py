def searchInArray(strs, target):
    if target not in strs:
        return -1 

    hashmap = {}

    for index, s in enumerate(strs):
        if s == "":
            continue
        hashmap[s] = index
    
    print(hashmap)

    return hashmap[target]


strs = ["apple", "", "", "", "banana", "", "cherry", "", ""]

print(searchInArray(strs, "apple"))