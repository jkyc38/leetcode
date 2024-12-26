from typing import List
import heapq

class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:

        boxTypes.sort(key=lambda x:x[1], reverse=True) #sort by the second element in the 2d array

        #basically sorts by the number of units 

        totalUnits = 0
        truckSizeleft = truckSize

        for numBoxes, numUnits in boxTypes:
            #calculate how many boxes we can take
            boxesToTake = min(truckSizeleft, numBoxes)

            if truckSizeleft<=0:
                break
            totalUnits += numUnits * boxesToTake
            truckSizeleft -= numBoxes


        return totalUnits


boxTypes = [[5,10],[2,5],[4,7],[3,9]]
heapq.heapify(boxTypes)


print(boxTypes)
print(type(boxTypes))