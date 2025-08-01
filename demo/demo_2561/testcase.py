from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[4, 2, 2, 2], [1, 4, 1, 2]], Output=1))
		self.testcases.append(case(Input=[[2, 3, 4, 1], [3, 2, 5, 1]], Output=-1))

	def get_testcases(self):
		return self.testcases
