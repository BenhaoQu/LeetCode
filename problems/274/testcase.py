from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=[3, 0, 6, 1, 5], Output=3))
        self.testcases.append(case(Input=[1, 3, 1], Output=1))
        self.testcases.append(case(Input=[1], Output=1))
        self.testcases.append(case(Input=[0], Output=0))

    def get_testcases(self):
        return self.testcases
