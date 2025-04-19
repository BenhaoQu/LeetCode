//go:build ignore
#include "cpp/common/Solution.h"
#include <stack>

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  vector<int> dailyTemperatures(vector<int> &temperatures) {
    int n = static_cast<int>(temperatures.size());
    vector<int> ans(n, 0);
    stack<int> st;
    for (int i = 0; i < n; i++) {
      while (!st.empty() && temperatures[i] > temperatures[st.top()]) {
        int pre = st.top();
        st.pop();
        ans[pre] = i - pre;
      }
      st.push(i);
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
  vector<int> temperatures = json::parse(inputArray.at(0));
  return solution.dailyTemperatures(temperatures);
}
