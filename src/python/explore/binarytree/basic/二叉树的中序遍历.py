#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   二叉树的中序遍历.py
@Time    :   2020/08/14 21:42:21
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
import os
import sys
import unittest

from typing import List

cur_dir = os.path.dirname(os.path.abspath(__file__))
py_dir = os.path.abspath(os.path.join(cur_dir, *(['..'] * 3)))
sys.path.append(py_dir)

from common.treenode import mkTreeFromPreAndIn  # noqa: E402
from common.treenode import TreeNode  # noqa: E402


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        # return self.recursiveTraversal(root)
        return self.iterateTraversal(root)

    def recursiveTraversal(self, root: TreeNode) -> List[int]:
        res = []
        self.recursive(root, res)
        return res

    @classmethod
    def recursive(cls, root: TreeNode, res: List[int]) -> None:
        if not root:
            return

        # 遍历左子树
        cls.recursive(root.left, res)
        # 访问当前树的根结点
        res.append(root.val)
        # 遍历右子树
        cls.recursive(root.right, res)

    def iterateTraversal(self, root: TreeNode) -> List[int]:
        return self.iterate(root)

    @classmethod
    def iterate(cls, root: TreeNode) -> List[int]:
        """迭代地进行中序遍历

        创建一个辅助栈：
        1.当前结点置为根结点
        2.如果当前结点不为空，则将最左路径的所有结点压入栈中
        3.弹出栈顶结点作为当前结点，将结点值追加到结果序列的尾部
        4.然后将当前结点置为当前结点的右子结点
        5.重复步骤2、3、4，直至当前结点为空且栈空

        Args:
            root (TreeNode): 树的根结点

        Returns:
            List[int]: 中序遍历结果
        """
        res = []
        stack = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left

            root = stack.pop()
            res.append(root.val)
            root = root.right

        return res


class TestPreorder(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.pre = [8, 4, 2, 1, 3, 6, 5, 7, 12, 10, 9, 11, 14, 13, 16, 15]
        cls.ino = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
        cls.root = mkTreeFromPreAndIn(cls.pre, cls.ino)

    def test_recursive_traversal(self):
        ans = Solution().recursiveTraversal(self.root)
        self.assertListEqual(ans, self.ino)

    def test_iterate_traversal(self):
        ans = Solution().iterateTraversal(self.root)
        self.assertListEqual(ans, self.ino)


if __name__ == '__main__':
    unittest.main()
