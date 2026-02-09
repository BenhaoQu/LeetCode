import solution
from typing import *
from python.object_libs import call_method


class Solution(solution.Solution):
    def solve(self, test_input=None):
        ops, inputs = test_input
        obj = OrderedStream(*inputs[0])
        return [None] + [call_method(obj, op, *ipt) for op, ipt in zip(ops[1:], inputs[1:])]


class OrderedStream:
    def __init__(self, n: int):
        pass

    def insert(self, idKey: int, value: str) -> List[str]:
        pass

