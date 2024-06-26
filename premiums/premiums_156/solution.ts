import {TreeNode,TreeNodeToJSONArray,JSONArrayToTreeNode} from "../../typescript/models/treenode";

/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     val: number
 *     left: TreeNode | null
 *     right: TreeNode | null
 *     constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.left = (left===undefined ? null : left)
 *         this.right = (right===undefined ? null : right)
 *     }
 * }
 */

function upsideDownBinaryTree(root: TreeNode | null): TreeNode | null {
    let node: TreeNode | null = null, left: TreeNode | null = root, right: TreeNode | null = null;
	while (left != null) {
		let newLeft: TreeNode | null = left.left, newRight: TreeNode | null = left.right;
		left.left = right;
		left.right = node;
		node = left;
		left = newLeft;
		right = newRight;
	}
	return node;
};

export function Solve(inputJsonElement: string): any {
	const splits: string[] = inputJsonElement.split("\n");
	const root: TreeNode | null = JSONArrayToTreeNode(JSON.parse(splits[0]));
	return TreeNodeToJSONArray(upsideDownBinaryTree(root));
}
