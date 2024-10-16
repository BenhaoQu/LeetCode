from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[1, 2], [3], [3], []], Output=[[0, 1, 3], [0, 2, 3]]))
		self.testcases.append(case(Input=[[4, 3, 1], [3, 2, 4], [3], [4], []], Output=[[0, 4], [0, 3, 4], [0, 1, 3, 4], [0, 1, 2, 3, 4], [0, 1, 4]]))
		self.testcases.append(case(Input=[[1], []], Output=[[0, 1]]))
		self.testcases.append(case(Input=[[1, 2, 3], [2], [3], []], Output=[[0, 1, 2, 3], [0, 2, 3], [0, 3]]))
		self.testcases.append(case(Input=[[1, 3], [2], [3], []], Output=[[0, 1, 2, 3], [0, 3]]))

	def get_testcases(self):
		return self.testcases