from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[5, 3, 4, 5], Output=True))
		self.testcases.append(case(Input=[3, 7, 2, 3], Output=True))

	def get_testcases(self):
		return self.testcases
