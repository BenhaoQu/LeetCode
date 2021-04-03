from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=[42, 11, 1, 97], Output=2))
        self.testcases.append(case(Input=[13, 10, 35, 24, 76], Output=4))

    def get_testcases(self):
        return self.testcases
