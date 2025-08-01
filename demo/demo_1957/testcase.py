from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input="leeetcode", Output="leetcode"))
		self.testcases.append(case(Input="aaabaaaa", Output="aabaa"))
		self.testcases.append(case(Input="aab", Output="aab"))

	def get_testcases(self):
		return self.testcases
