from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[-1, 0, 1, 2, -1, -4], Output=[[-1, -1, 2], [-1, 0, 1]]))
		self.testcases.append(case(Input=[], Output=[]))
		self.testcases.append(case(Input=[0], Output=[]))
		self.testcases.append(case(Input=[-2,0,1,1,2], Output=[[-2,0,2],[-2,1,1]]))

	def get_testcases(self):
		return self.testcases
