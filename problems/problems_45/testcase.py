from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[2, 3, 1, 1, 4], Output=2))
		self.testcases.append(case(Input=[2, 3, 0, 1, 4], Output=2))

	def get_testcases(self):
		return self.testcases
