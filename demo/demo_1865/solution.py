import solution
from typing import *
from python.object_libs import call_method


class Solution(solution.Solution):
    def solve(self, test_input=None):
        ops, inputs = test_input
        obj = FindSumPairs(*inputs[0])
        return [None] + [call_method(obj, op, *ipt) for op, ipt in zip(ops[1:], inputs[1:])]


class FindSumPairs:
    def __init__(self, nums1: List[int], nums2: List[int]):
        pass

    def add(self, index: int, val: int) -> None:
        pass

    def count(self, tot: int) -> int:
        pass

