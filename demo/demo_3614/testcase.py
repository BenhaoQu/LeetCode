from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=['a#b%*', 1], Output="a"))
		self.testcases.append(case(Input=['cd%#*#', 3], Output="d"))
		self.testcases.append(case(Input=['z*#', 0], Output="."))

	def get_testcases(self):
		return self.testcases
