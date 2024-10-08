from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[1, 3, 4], [1, 3, 4], 1], Output=5))
		self.testcases.append(case(Input=[[1, 2, 4, 12], [2, 4], 3], Output=2))

	def get_testcases(self):
		return self.testcases
