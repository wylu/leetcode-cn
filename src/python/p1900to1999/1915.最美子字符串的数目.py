#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   1915.最美子字符串的数目.py
@Time    :   2021/07/04 17:21:27
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=1915 lang=python3
#
# [1915] 最美子字符串的数目
#
# https://leetcode-cn.com/problems/number-of-wonderful-substrings/description/
#
# algorithms
# Medium (36.66%)
# Likes:    44
# Dislikes: 0
# Total Accepted:    2.3K
# Total Submissions: 6.1K
# Testcase Example:  '"aba"'
#
# 如果某个字符串中 至多一个 字母出现 奇数 次，则称其为 最美 字符串。
#
#
# 例如，"ccjjc" 和 "abab" 都是最美字符串，但 "ab" 不是。
#
#
# 给你一个字符串 word ，该字符串由前十个小写英文字母组成（'a' 到 'j'）。请你返回 word 中 最美非空子字符串 的数目。如果同样的子字符串在
# word 中出现多次，那么应当对 每次出现 分别计数。
#
# 子字符串 是字符串中的一个连续字符序列。
#
#
#
# 示例 1：
#
#
# 输入：word = "aba"
# 输出：4
# 解释：4 个最美子字符串如下所示：
# - "aba" -> "a"
# - "aba" -> "b"
# - "aba" -> "a"
# - "aba" -> "aba"
#
#
# 示例 2：
#
#
# 输入：word = "aabb"
# 输出：9
# 解释：9 个最美子字符串如下所示：
# - "aabb" -> "a"
# - "aabb" -> "aa"
# - "aabb" -> "aab"
# - "aabb" -> "aabb"
# - "aabb" -> "a"
# - "aabb" -> "abb"
# - "aabb" -> "b"
# - "aabb" -> "bb"
# - "aabb" -> "b"
#
#
# 示例 3：
#
#
# 输入：word = "he"
# 输出：2
# 解释：2 个最美子字符串如下所示：
# - "he" -> "h"
# - "he" -> "e"
#
#
#
#
# 提示：
#
#
# 1 <= word.length <= 10^5
# word 由从 'a' 到 'j' 的小写英文字母组成
#
#
#
from collections import defaultdict


# @lc code=start
class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        cnt = defaultdict(int)
        cnt[0] += 1
        state = 0

        ans = 0
        for ch in word:
            c = ord(ch) - ord('a')
            state ^= (1 << c)

            ans += cnt[state]
            for i in range(10):
                ans += cnt[state ^ (1 << i)]

            cnt[state] += 1

        return ans


# @lc code=end

if __name__ == '__main__':
    solu = Solution()
    print(solu.wonderfulSubstrings(word="aba"))
    print(solu.wonderfulSubstrings(word="aabb"))
    print(solu.wonderfulSubstrings(word="he"))
