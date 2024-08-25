from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[1, 2, 3], Output=[[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]))
		self.testcases.append(case(Input=[0], Output=[[], [0]]))

	def get_testcases(self):
		return self.testcases
