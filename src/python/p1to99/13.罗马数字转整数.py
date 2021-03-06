#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   13.罗马数字转整数.py
@Time    :   2020/08/05 22:27:30
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=13 lang=python3
#
# [13] 罗马数字转整数
#
# https://leetcode-cn.com/problems/roman-to-integer/description/
#
# algorithms
# Easy (61.91%)
# Likes:    980
# Dislikes: 0
# Total Accepted:    234.6K
# Total Submissions: 378.8K
# Testcase Example:  '"III"'
#
# 罗马数字包含以下七种字符: I， V， X， L，C，D 和 M。
#
# 字符          数值
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
#
# 例如， 罗马数字 2 写做 II ，即为两个并列的 1。12 写做 XII ，即为 X + II 。 27 写做  XXVII, 即为 XX + V +
# II 。
#
# 通常情况下，罗马数字中小的数字在大的数字的右边。但也存在特例，例如 4 不写做 IIII，而是 IV。数字 1 在数字 5 的左边，所表示的数等于大数 5
# 减小数 1 得到的数值 4 。同样地，数字 9 表示为 IX。这个特殊的规则只适用于以下六种情况：
#
#
# I 可以放在 V (5) 和 X (10) 的左边，来表示 4 和 9。
# X 可以放在 L (50) 和 C (100) 的左边，来表示 40 和 90。
# C 可以放在 D (500) 和 M (1000) 的左边，来表示 400 和 900。
#
#
# 给定一个罗马数字，将其转换成整数。输入确保在 1 到 3999 的范围内。
#
# 示例 1:
#
# 输入: "III"
# 输出: 3
#
# 示例 2:
#
# 输入: "IV"
# 输出: 4
#
# 示例 3:
#
# 输入: "IX"
# 输出: 9
#
# 示例 4:
#
# 输入: "LVIII"
# 输出: 58
# 解释: L = 50, V= 5, III = 3.
#
#
# 示例 5:
#
# 输入: "MCMXCIV"
# 输出: 1994
# 解释: M = 1000, CM = 900, XC = 90, IV = 4.
#
#
"""
方法一：模拟
思路

通常情况下，罗马数字中小的数字在大的数字的右边。若输入的字符串满足该情况，
那么可以将每个字符视作一个单独的值，累加每个字符对应的数值即可。

例如 XXVII 可视作 X+X+V+I+I = 10+10+5+1+1 = 27。

若存在小的数字在大的数字的左边的情况，根据规则需要减去小的数字。对于这种
情况，我们也可以将每个字符视作一个单独的值，若一个数字右侧的数字比它大，
则将该数字的符号取反。

例如 XIV 可视作 X-I+V = 10-1+5 = 14。
"""


# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        symbolValues = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        ans = symbolValues[s[-1]]
        for i in range(len(s) - 1):
            if symbolValues[s[i]] < symbolValues[s[i + 1]]:
                ans -= symbolValues[s[i]]
            else:
                ans += symbolValues[s[i]]

        return ans


# @lc code=end

# class Solution:
#     def romanToInt(self, s: str) -> int:
#         if not s:
#             return 0

#         roma = {
#             'I': 1,
#             'V': 5,
#             'X': 10,
#             'L': 50,
#             'C': 100,
#             'D': 500,
#             'M': 1000
#         }

#         ans = 0
#         i = len(s) - 1
#         while i >= 0:
#             ans += roma[s[i]]

#             if i > 0:
#                 if (s[i] == 'V' or s[i] == 'X') and s[i - 1] == 'I':
#                     ans -= 1
#                     i -= 1
#                 elif (s[i] == 'L' or s[i] == 'C') and s[i - 1] == 'X':
#                     ans -= 10
#                     i -= 1
#                 elif (s[i] == 'D' or s[i] == 'M') and s[i - 1] == 'C':
#                     ans -= 100
#                     i -= 1

#             i -= 1

#         return ans
