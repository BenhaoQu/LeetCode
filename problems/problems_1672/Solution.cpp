//go:build ignore
#include "cpp/common/Solution.h"
#include <numeric>


using namespace std;
using json = nlohmann::json;

class Solution {
public:
    int maximumWealth(vector<vector<int>>& accounts) {
        int ans = 0;
        for (auto account: accounts) {
            ans = max(ans, std::accumulate(account.begin(), account.end(), 0));
        }
        return ans;
    }
};

json leetcode::qubh::Solve(string input)
{
	vector<string> inputArray;
	size_t pos = input.find('\n');
	while (pos != string::npos) {
		inputArray.push_back(input.substr(0, pos));
		input = input.substr(pos + 1);
		pos = input.find('\n');
	}
	inputArray.push_back(input);

	Solution solution;
	vector<vector<int>> accounts = json::parse(inputArray.at(0));
	return solution.maximumWealth(accounts);
}
