import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        root_nums = test_input
        root = TreeNode(root_nums.pop(0))
        while root_nums:
            last = curr = root
            num = root_nums.pop(0)
            if num:
                L = False
                while curr:
                    if num < curr.val:
                        last = curr
                        curr = curr.left
                        L = True
                    else:
                        last = curr
                        curr = curr.right
                        L = False
                if L:
                    last.setL(TreeNode(val=num))
                else:
                    last.setR(TreeNode(val=num))

        arr = []
        node = self.increasingBST(root)
        while node:
            arr.append(node.val)
            node = node.right
            if node:
                arr.append(None)
        return arr

    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        # if not root:
        #     return
        # if root.left:
        #     temp = root
        #     root = self.increasingBST(root.left)
        #     temp.left = None
        #     curr = root
        #     while curr.right:
        #         curr = curr.right
        #     curr.right = temp
        #     temp.right = self.increasingBST(temp.right)
        # elif root.right:
        #     root.right = self.increasingBST(root.right)
        # return root

        def reorder_BST(root, tail=None):
            if not root:
                return tail
            res = reorder_BST(root.left, root)
            root.left = None
            root.right = reorder_BST(root.right, tail)
            return res
        return reorder_BST(root)

        # parent = node = root
        # while node:
        #     if node.left:
        #         temp = curr = node.left
        #         while curr.right:
        #             curr = curr.right
        #         curr.right = node
        #         node.left = None
        #         if parent == node:
        #             root = temp
        #             parent = node = root
        #         else:
        #             parent.right = temp
        #             node = parent
        #     else:
        #         parent = node
        #         node = node.right
        # return root


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def setL(self, left):
        self.left = left

    def setR(self, right):
        self.right = right
