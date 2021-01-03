import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.countPairs(list(test_input))

    def countPairs(self, deliciousness):
        """
        :type deliciousness: List[int]
        :rtype: int
        """
        import collections
        ans = 0
        freq = collections.defaultdict(int)
        for x in deliciousness:
            for k in range(22): ans += freq[2**k - x]
            freq[x] += 1
        return ans % (10**9 + 7)
