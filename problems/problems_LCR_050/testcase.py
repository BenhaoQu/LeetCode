from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[10, 5, -3, 3, 2, None, 11, 3, -2, None, 1], 8], Output=3))
		self.testcases.append(case(Input=[[5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1], 22], Output=3))

	def get_testcases(self):
		return self.testcases
