from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[1, 2], [2, 3], [3, 4]], Output=3))
		self.testcases.append(case(Input=[[1, 2], [2, 3], [3, 4], [1, 2]], Output=4))

	def get_testcases(self):
		return self.testcases
