from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[5, [1, 3], [2, 5]], Output=2))
		self.testcases.append(case(Input=[10, [0, 7, 9], [1, 8, 10]], Output=7))
		self.testcases.append(case(Input=[10, [0, 3, 7, 9], [1, 4, 8, 10]], Output=6))
		self.testcases.append(case(Input=[5, [0, 1, 2, 3, 4], [1, 2, 3, 4, 5]], Output=0))

	def get_testcases(self):
		return self.testcases
