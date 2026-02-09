from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[4, 2, 4, 5, 6], Output=17))
		self.testcases.append(case(Input=[5, 2, 1, 2, 5, 2, 1, 2, 5], Output=8))

	def get_testcases(self):
		return self.testcases
