from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[3, 6, 1, 3, 4], [2, 1, 3, 4, 5], 25], Output=3))
		self.testcases.append(case(Input=[[11, 12, 19], [10, 8, 7], 19], Output=0))

	def get_testcases(self):
		return self.testcases
