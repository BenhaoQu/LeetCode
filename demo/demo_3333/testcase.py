from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=['aabbccdd', 7], Output=5))
		self.testcases.append(case(Input=['aabbccdd', 8], Output=1))
		self.testcases.append(case(Input=['aaabbb', 3], Output=8))

	def get_testcases(self):
		return self.testcases
