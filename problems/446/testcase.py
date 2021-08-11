from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=[2, 4, 6, 8, 10], Output=7))
        self.testcases.append(case(Input=[7, 7, 7, 7, 7], Output=16))

    def get_testcases(self):
        return self.testcases
