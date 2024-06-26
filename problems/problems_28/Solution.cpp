//go:build ignore
#include "cpp/common/Solution.h"


using namespace std;
using json = nlohmann::json;

class Solution {
public:
    int strStr(string haystack, string needle) {
        return haystack.find(needle);
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
	string haystack = json::parse(inputArray.at(0));
	string needle = json::parse(inputArray.at(1));
	return solution.strStr(haystack, needle);
}
