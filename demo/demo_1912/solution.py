import solution
from typing import *
from python.object_libs import call_method


class Solution(solution.Solution):
    def solve(self, test_input=None):
        ops, inputs = test_input
        obj = MovieRentingSystem(*inputs[0])
        return [None] + [call_method(obj, op, *ipt) for op, ipt in zip(ops[1:], inputs[1:])]


class MovieRentingSystem:
    def __init__(self, n: int, entries: List[List[int]]):
        pass

    def search(self, movie: int) -> List[int]:
        pass

    def rent(self, shop: int, movie: int) -> None:
        pass

    def drop(self, shop: int, movie: int) -> None:
        pass

    def report(self) -> List[List[int]]:
        pass

