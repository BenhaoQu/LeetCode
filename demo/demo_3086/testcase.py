from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[1, 1, 0, 0, 0, 1, 1, 0, 0, 1], 3, 1], Output=None))
		self.testcases.append(case(Input=[[0, 0, 0, 0], 2, 3], Output=None))

	def get_testcases(self):
		return self.testcases
