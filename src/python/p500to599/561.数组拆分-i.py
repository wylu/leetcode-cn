#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   561.数组拆分-i.py
@Time    :   2020/10/02 16:33:13
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=561 lang=python3
#
# [561] 数组拆分 I
#
# https://leetcode-cn.com/problems/array-partition-i/description/
#
# algorithms
# Easy (72.13%)
# Likes:    190
# Dislikes: 0
# Total Accepted:    48.4K
# Total Submissions: 67.1K
# Testcase Example:  '[1,4,3,2]'
#
# 给定长度为 2n 的数组, 你的任务是将这些数分成 n 对, 例如 (a1, b1), (a2, b2), ..., (an, bn) ，使得从1 到 n
# 的 min(ai, bi) 总和最大。
#
# 示例 1:
#
#
# 输入: [1,4,3,2]
#
# 输出: 4
# 解释: n 等于 2, 最大总和为 4 = min(1, 2) + min(3, 4).
#
#
# 提示:
#
#
# n 是正整数,范围在 [1, 10000].
# 数组中的元素范围在 [-10000, 10000].
#
#
#
from typing import List


# @lc code=start
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        ans = 0
        for i in range(0, len(nums), 2):
            ans += min(nums[i], nums[i + 1])
        return ans


# @lc code=end
