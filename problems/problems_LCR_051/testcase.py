from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[1, 2, 3], Output=6))
		self.testcases.append(case(Input=[-10, 9, 20, None, None, 15, 7], Output=42))
		self.testcases.append(case(Input=[2,-1], Output=2))
		self.testcases.append(case(Input=[1,-2,3], Output=4))
		self.testcases.append(case(Input=[2,-1,-2], Output=2))

	def get_testcases(self):
		return self.testcases
