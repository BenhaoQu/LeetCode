//go:build ignore
#include "cpp/common/Solution.h"
#include "cpp/models/TreeNode.h"

using namespace std;
using json = nlohmann::json;

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    bool isSameTree(TreeNode* p, TreeNode* q) {
        return (p == nullptr && q == nullptr) || (p != nullptr && q != nullptr && p->val == q->val && isSameTree(p->left, q->left) && isSameTree(p->right, q->right));
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
	json p_array = json::parse(inputArray.at(0));
	TreeNode *p = JsonArrayToTreeNode(p_array);
	json q_array = json::parse(inputArray.at(1));
	TreeNode *q = JsonArrayToTreeNode(q_array);
	return solution.isSameTree(p, q);
}
