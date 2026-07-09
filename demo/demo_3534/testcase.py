from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[5, [1, 8, 3, 4, 2], 3, [[0, 3], [2, 4]]], Output=[1, 1]))
		self.testcases.append(case(Input=[5, [5, 3, 1, 9, 10], 2, [[0, 1], [0, 2], [2, 3], [4, 3]]], Output=[1, 2, -1, 1]))
		self.testcases.append(case(Input=[3, [3, 6, 1], 1, [[0, 0], [0, 1], [1, 2]]], Output=[0, -1, -1]))

	def get_testcases(self):
		return self.testcases
