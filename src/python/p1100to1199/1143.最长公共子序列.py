#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   1143.最长公共子序列.py
@Time    :   2021/04/03 11:10:30
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=1143 lang=python3
#
# [1143] 最长公共子序列
#
# https://leetcode-cn.com/problems/longest-common-subsequence/description/
#
# algorithms
# Medium (61.71%)
# Likes:    438
# Dislikes: 0
# Total Accepted:    88.3K
# Total Submissions: 143.1K
# Testcase Example:  '"abcde"\n"ace"'
#
# 给定两个字符串 text1 和 text2，返回这两个字符串的最长 公共子序列 的长度。如果不存在 公共子序列 ，返回 0 。
#
# 一个字符串的 子序列
# 是指这样一个新的字符串：它是由原字符串在不改变字符的相对顺序的情况下删除某些字符（也可以不删除任何字符）后组成的新字符串。
#
#
# 例如，"ace" 是 "abcde" 的子序列，但 "aec" 不是 "abcde" 的子序列。
#
#
# 两个字符串的 公共子序列 是这两个字符串所共同拥有的子序列。
#
#
#
# 示例 1：
#
#
# 输入：text1 = "abcde", text2 = "ace"
# 输出：3
# 解释：最长公共子序列是 "ace" ，它的长度为 3 。
#
#
# 示例 2：
#
#
# 输入：text1 = "abc", text2 = "abc"
# 输出：3
# 解释：最长公共子序列是 "abc" ，它的长度为 3 。
#
#
# 示例 3：
#
#
# 输入：text1 = "abc", text2 = "def"
# 输出：0
# 解释：两个字符串没有公共子序列，返回 0 。
#
#
#
#
# 提示：
#
#
# 1 <= text1.length, text2.length <= 1000
# text1 和 text2 仅由小写英文字符组成。
#
#
#
"""
Dynamic Programming

State:
  dp[i][j]: 表以 text1[0...i], text2[0...j] 的最长公共子序列的长度

Initial State:
  dp[i][0] = 0
  dp[0][j] = 0

State Transition:
  if text1[i] == text2[j]:
      dp[i][j] = dp[i-1][j-1] + 1
  else:
      dp[i][j] = max(dp[i][j-1], dp[i-1][j])
"""


# @lc code=start
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m):
            for j in range(n):
                if text1[i] == text2[j]:
                    dp[i + 1][j + 1] = dp[i][j] + 1
                else:
                    dp[i + 1][j + 1] = max(dp[i + 1][j], dp[i][j + 1])

        return dp[m][n]


# @lc code=end

if __name__ == '__main__':
    solu = Solution()
    print(solu.longestCommonSubsequence(text1="abcde", text2="ace"))
    print(solu.longestCommonSubsequence(text1="abc", text2="abc"))
    print(solu.longestCommonSubsequence(text1="abc", text2="def"))
