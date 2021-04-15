from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=[2, 3, 2], Output=3))
        self.testcases.append(case(Input=[1, 2, 3, 1], Output=4))
        self.testcases.append(case(Input=[0], Output=0))
        self.testcases.append(case(Input=[1, 3, 1, 3, 100], Output=103))
        self.testcases.append(case(Input=[1], Output=1))
        self.testcases.append(case(Input=[1, 3], Output=3))

    def get_testcases(self):
        return self.testcases
