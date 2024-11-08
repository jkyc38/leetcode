def maxSubarrayDivByK(nums, k):
    l = 0
    current_sum = 0
    max_len = 0
    
    for r in range(len(nums)):
        # Expand the window by adding nums[r] to the current_sum
        current_sum += nums[r]
        
        # Check if the current sum is divisible by k
        if current_sum % k == 0:
            # If divisible, calculate the length and update max_len
            max_len = max(max_len, r - l + 1)
        
        # (Optionally) if you want to keep trying different windows by shrinking from the left,
        # only shrink when it's necessary, like exploring a new sum that may be divisible by k later.
        # You can remove this part and instead explore just by expanding 'r'.
        
        # You could do this if you need to shrink for some reason
        # while current_sum % k != 0 and l <= r:
        #     current_sum -= nums[l]
        #     l += 1

    return max_len


nums = [612, 345, 34, 990, 1]
k = 3
sol = maxSubarrayDivByK(nums, k)

print(sol)