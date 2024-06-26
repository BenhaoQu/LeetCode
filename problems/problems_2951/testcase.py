from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[2, 4, 4], Output=[]))
		self.testcases.append(case(Input=[1, 4, 3, 8, 5], Output=[1, 3]))

	def get_testcases(self):
		return self.testcases
