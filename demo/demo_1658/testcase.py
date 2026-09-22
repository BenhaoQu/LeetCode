from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[1, 1, 4, 2, 3], 5], Output=2))
		self.testcases.append(case(Input=[[5, 6, 7, 8, 9], 4], Output=-1))
		self.testcases.append(case(Input=[[3, 2, 20, 1, 1, 3], 10], Output=5))

	def get_testcases(self):
		return self.testcases
