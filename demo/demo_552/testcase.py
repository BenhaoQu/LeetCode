from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=2, Output=8))
		self.testcases.append(case(Input=1, Output=3))
		self.testcases.append(case(Input=10101, Output=183236316))

	def get_testcases(self):
		return self.testcases
