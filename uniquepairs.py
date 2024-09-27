def uniquePairs(nums, target):
    res = {}
    out = set()

    for index, value in enumerate(nums):
        if target - value in res:
            out.add((value, target-value))
        else:
            res[value]=index

    return len(out)


def find_pairs(a, b, target):
    # Step 1: Create a hash map for array 'a'
    a_map = {}
    for i, num in enumerate(a):
        a_map[num] = i  # Store the index or count if needed
    
    # Step 2: Find pairs
    result = []
    for j, num in enumerate(b):
        complement = target - num
        if complement in a_map:
            result.append((a_map[complement], j))  # Pair of indices (i, j)
    
    return result


def uniquePairs(nums, target):
    res = {}
    out = set()

    for index, value in enumerate(nums):
        if target - value in res:
            out.add((value, target-value))
        if value not in res:
            res[value] = index
            

    return len(out)