from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=None, Output=3))
		self.testcases.append(case(Input=None, Output=6))

	def get_testcases(self):
		return self.testcases
