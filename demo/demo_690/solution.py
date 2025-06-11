import solution
from typing import *



# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates


class Solution(solution.Solution):
    def solve(self, test_input=None):
        employees, id = test_input
        return self.getImportance(employees, id)

    def getImportance(self, employees: List['Employee'], id: int) -> int:
        pass

