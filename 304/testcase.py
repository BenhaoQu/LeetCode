from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(
            Input=([[[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]], (2, 1, 4, 3),
                    (1, 1, 2, 2), (1, 2, 2, 4)]),
            Output=[None, 8, 11, 12]))

    def get_testcases(self):
        return self.testcases
