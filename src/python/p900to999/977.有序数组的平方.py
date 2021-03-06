#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   977.有序数组的平方.py
@Time    :   2020/10/16 09:11:53
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=977 lang=python3
#
# [977] 有序数组的平方
#
# https://leetcode-cn.com/problems/squares-of-a-sorted-array/description/
#
# algorithms
# Easy (71.65%)
# Likes:    136
# Dislikes: 0
# Total Accepted:    54.1K
# Total Submissions: 74.7K
# Testcase Example:  '[-4,-1,0,3,10]'
#
# 给定一个按非递减顺序排序的整数数组 A，返回每个数字的平方组成的新数组，要求也按非递减顺序排序。
#
#
#
# 示例 1：
#
# 输入：[-4,-1,0,3,10]
# 输出：[0,1,9,16,100]
#
#
# 示例 2：
#
# 输入：[-7,-3,2,3,11]
# 输出：[4,9,9,49,121]
#
#
#
#
# 提示：
#
#
# 1 <= A.length <= 10000
# -10000 <= A[i] <= 10000
# A 已按非递减顺序排序。
#
#
#
from typing import List
"""
双指针

思路与算法

我们可以使用两个指针分别指向位置 0 和 n−1，每次比较两个指针对应的数，
选择较大的那个逆序放入答案并移动指针。这种方法无需处理某一指针移动至
边界的情况。
"""


# @lc code=start
class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        n = len(A)
        ans = [0] * n

        i, j, k = 0, n - 1, n - 1
        while i <= j:
            if A[i] * A[i] > A[j] * A[j]:
                ans[k] = A[i] * A[i]
                i += 1
            else:
                ans[k] = A[j] * A[j]
                j -= 1
            k -= 1

        return ans


# @lc code=end

# class Solution:
#     def sortedSquares(self, A: List[int]) -> List[int]:
#         for i in range(len(A)):
#             A[i] *= A[i]
#         A.sort()
#         return A

if __name__ == "__main__":
    solu = Solution()
    print(solu.sortedSquares([-4, -1, 0, 3, 10]))
