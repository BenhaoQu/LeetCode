from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=['1.2', '1.10'], Output=-1))
		self.testcases.append(case(Input=['1.01', '1.001'], Output=0))
		self.testcases.append(case(Input=['1.0', '1.0.0.0'], Output=0))

	def get_testcases(self):
		return self.testcases
