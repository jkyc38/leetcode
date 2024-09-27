from collections import deque
from typing import List

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:

        students_q = deque(students)
        sw_q = deque(sandwiches)
        count = 0 
        while sw_q and count!=len(students_q):
            student = students_q.popleft()
            sw = sw_q.popleft()

            if student == sw:
                count = 0
                continue
            else:
                students_q.append(student)
                sw_q.appendleft(sw)
                count+=1

        return len(students_q)




q = [3,4,2,4]

q = deque(q)
print(q)
# q.popleft()
q.appendleft(35)
print(q)

print(len(q))