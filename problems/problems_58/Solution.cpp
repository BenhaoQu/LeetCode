//go:build ignore
#include "cpp/common/Solution.h"


using namespace std;
using json = nlohmann::json;

class Solution {
public:
    int lengthOfLastWord(string s) {
        int idx, i;
        for (idx = s.length() - 1; idx >= 0 && s[idx] == ' '; idx--) {}
        for (i = idx - 1; i >= 0 && s[i] != ' '; i--) {}
        return idx - i;
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
	string s = json::parse(inputArray.at(0));
	return solution.lengthOfLastWord(s);
}
