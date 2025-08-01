from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[11, 2, 4], Output=[3, 4]))
		self.testcases.append(case(Input=[5, 1, 5], Output=[1, 1]))

	def get_testcases(self):
		return self.testcases
