from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[['Robot', 'step', 'step', 'getPos', 'getDir', 'step', 'step', 'step', 'getPos', 'getDir'], [[6, 3], [2], [2], [], [], [2], [1], [4], [], []]], Output=[None, None, None, [4, 0], 'East', None, None, None, [1, 2], 'West']))

	def get_testcases(self):
		return self.testcases
