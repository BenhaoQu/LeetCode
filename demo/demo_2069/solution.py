import solution
from typing import *
from python.object_libs import call_method


class Solution(solution.Solution):
    def solve(self, test_input=None):
        ops, inputs = test_input
        obj = Robot(*inputs[0])
        return [None] + [call_method(obj, op, *ipt) for op, ipt in zip(ops[1:], inputs[1:])]


class Robot:
    def __init__(self, width: int, height: int):
        pass

    def step(self, num: int) -> None:
        pass

    def getPos(self) -> List[int]:
        pass

    def getDir(self) -> str:
        pass

