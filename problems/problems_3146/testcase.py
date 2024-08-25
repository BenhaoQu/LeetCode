from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=['abc', 'bac'], Output=2))
		self.testcases.append(case(Input=['abcde', 'edbac'], Output=12))

	def get_testcases(self):
		return self.testcases
