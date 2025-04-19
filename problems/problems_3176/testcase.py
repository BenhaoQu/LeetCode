from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[1, 2, 1, 1, 3], 2], Output=4))
		self.testcases.append(case(Input=[[1, 2, 3, 4, 5, 1], 0], Output=2))

	def get_testcases(self):
		return self.testcases
