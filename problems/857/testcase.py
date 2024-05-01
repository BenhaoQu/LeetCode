from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[10, 20, 5], [70, 50, 30], 2], Output=105.0))
		self.testcases.append(case(Input=[[3, 1, 10, 10, 1], [4, 8, 2, 2, 7], 3], Output=30.66667))

	def get_testcases(self):
		return self.testcases
