'''
You are given an integer array heights where heights[i] represents the height of the i-th bar
You may choose any two bars to form a container. Return the maximum amount of water a container can store.'''

#initiate two pointers in the beginning of array
#increment r pointer 
#get lowest height between the two pointers and multiply by the 
#distance between the two pointers
#if the area is greater than the current area then set it to the 
#next area

def maxArea(heights: list[int])-> int:
    l, r = 0, len(heights)-1
    
        #move left pointer
    area = 0 
    while l<r:
        h = min(heights[l], heights[r])
        length = r - l

        area = max(area, (length * h))

        if heights[l]> heights[r]:
            r-=1
        else:
            l+=1

    return area
    