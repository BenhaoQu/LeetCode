from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[2, 3, 6], Output=2))
		self.testcases.append(case(Input=[1, 4, 3], Output=2))

	def get_testcases(self):
		return self.testcases
