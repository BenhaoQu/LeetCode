//go:build ignore
#include "cpp/common/Solution.h"


using namespace std;
using json = nlohmann::json;

class Solution {
public:
    int maximumSum(vector<int>& arr) {
        auto ans = INT_MIN / 2, dp0 = ans, dp1 = ans;
        for (auto num: arr) {
            dp1 = max(dp1 + num, dp0);
            dp0 = max(dp0 + num, num);
            ans = max({ans, dp0, dp1});
        }
        return ans;
    }
};

json leetcode::qubh::Solve(string input_json_values) {
	vector<string> inputArray;
	size_t pos = input_json_values.find('\n');
	while (pos != string::npos) {
		inputArray.push_back(input_json_values.substr(0, pos));
		input_json_values = input_json_values.substr(pos + 1);
		pos = input_json_values.find('\n');
	}
	inputArray.push_back(input_json_values);

	Solution solution;
	vector<int> arr = json::parse(inputArray.at(0));
	return solution.maximumSum(arr);
}
