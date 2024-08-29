from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[1, 0, 2], [1, 0, 2]], Output=True))
		self.testcases.append(case(Input=[[1, 1, 1], [0, 0, 0]], Output=False))
		self.testcases.append(case(Input=[[1], [2], [3]], Output=False))
		self.testcases.append(case(Input=[[1,7],[1,1]], Output=False))

	def get_testcases(self):
		return self.testcases