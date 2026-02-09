from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[['####F', '#C...', 'M....'], 1, 2], Output=True))
		self.testcases.append(case(Input=[['M.C...F'], 1, 4], Output=True))
		self.testcases.append(case(Input=[['M.C...F'], 1, 3], Output=False))

	def get_testcases(self):
		return self.testcases
