import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.generateParenthesis(test_input)

    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        def backtrack(cur, left, right):
            if left == right == n:
                ans.append("".join(cur))
                return
            if left < n:
                cur.append("(")
                backtrack(cur, left + 1, right)
                cur.pop()
            if right < left:
                cur.append(")")
                backtrack(cur, left, right + 1)
                cur.pop()

        backtrack([], 0, 0)
        return ans
