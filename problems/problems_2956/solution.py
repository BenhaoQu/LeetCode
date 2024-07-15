import solution
from typing import *
from collections import Counter


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.findIntersectionValues(*test_input)

    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = [0, 0]
        counter = Counter(nums2)
        for i, num in enumerate(nums1):
            if num not in counter:
                continue
            ans[0] += 1
            ans[1] += counter[num]
            counter[num] = 0
        return ans
