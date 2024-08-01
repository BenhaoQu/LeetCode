from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[1, 2, 8, 9], 3], Output=18))
		self.testcases.append(case(Input=[[3, 3, 1], 1], Output=0))
		self.testcases.append(case(Input=[[10,3],1], Output=10))
		self.testcases.append(case(Input=[[1,3,4,5],4], Output=0))

	def get_testcases(self):
		return self.testcases
