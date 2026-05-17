from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[100, -23, -23, 404, 100, 23, 23, 23, 3, 404], Output=3))
		self.testcases.append(case(Input=[7], Output=0))
		self.testcases.append(case(Input=[7, 6, 9, 6, 9, 6, 9, 7], Output=1))

	def get_testcases(self):
		return self.testcases
