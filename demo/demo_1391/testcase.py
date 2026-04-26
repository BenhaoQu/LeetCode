from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[2, 4, 3], [6, 5, 2]], Output=True))
		self.testcases.append(case(Input=[[1, 2, 1], [1, 2, 1]], Output=False))
		self.testcases.append(case(Input=[[1, 1, 2]], Output=False))

	def get_testcases(self):
		return self.testcases
