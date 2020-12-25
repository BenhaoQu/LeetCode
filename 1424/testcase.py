from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=[[1, 2, 3], [4, 5, 6], [7, 8, 9]], Output=[1, 4, 2, 7, 5, 3, 8, 6, 9]))
        self.testcases.append(case(Input=[[1, 2, 3, 4, 5], [6, 7], [8], [9, 10, 11], [12, 13, 14, 15, 16]],
                                   Output=[1, 6, 2, 8, 7, 3, 9, 4, 12, 10, 5, 13, 11, 14, 15, 16]))
        self.testcases.append(
            case(Input=[[1, 2, 3], [4], [5, 6, 7], [8], [9, 10, 11]], Output=[1, 4, 2, 5, 3, 8, 6, 9, 7, 10, 11]))
        self.testcases.append(case(Input=[[1, 2, 3, 4, 5, 6]], Output=[1, 2, 3, 4, 5, 6]))

    def get_testcases(self):
        return self.testcases
