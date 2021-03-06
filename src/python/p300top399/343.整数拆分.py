#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   343.整数拆分.py
@Time    :   2020/07/30 00:15:52
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=343 lang=python3
#
# [343] 整数拆分
#
# https://leetcode-cn.com/problems/integer-break/description/
#
# algorithms
# Medium (56.36%)
# Likes:    260
# Dislikes: 0
# Total Accepted:    33.2K
# Total Submissions: 58.8K
# Testcase Example:  '2'
#
# 给定一个正整数 n，将其拆分为至少两个正整数的和，并使这些整数的乘积最大化。
# 返回你可以获得的最大乘积。
#
# 示例 1:
#
# 输入: 2
# 输出: 1
# 解释: 2 = 1 + 1, 1 × 1 = 1。
#
# 示例 2:
#
# 输入: 10
# 输出: 36
# 解释: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36。
#
# 说明: 你可以假设 n 不小于 2 且不大于 58。
#
#


# @lc code=start
class Solution:
    def integerBreak(self, n: int) -> int:
        if n <= 3:
            return n - 1

        a, b = n // 3, n % 3
        if b == 0:
            return pow(3, a)
        elif b == 1:
            return pow(3, a - 1) * 4
        else:
            return pow(3, a) * 2


# @lc code=end
