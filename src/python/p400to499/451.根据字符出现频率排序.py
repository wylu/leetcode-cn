#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   451.根据字符出现频率排序.py
@Time    :   2021/07/03 19:08:13
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=451 lang=python3
#
# [451] 根据字符出现频率排序
#
# https://leetcode-cn.com/problems/sort-characters-by-frequency/description/
#
# algorithms
# Medium (69.91%)
# Likes:    303
# Dislikes: 0
# Total Accepted:    64.8K
# Total Submissions: 92.7K
# Testcase Example:  '"tree"'
#
# 给定一个字符串，请将字符串里的字符按照出现的频率降序排列。
#
# 示例 1:
#
#
# 输入:
# "tree"
#
# 输出:
# "eert"
#
# 解释:
# 'e'出现两次，'r'和't'都只出现一次。
# 因此'e'必须出现在'r'和't'之前。此外，"eetr"也是一个有效的答案。
#
#
# 示例 2:
#
#
# 输入:
# "cccaaa"
#
# 输出:
# "cccaaa"
#
# 解释:
# 'c'和'a'都出现三次。此外，"aaaccc"也是有效的答案。
# 注意"cacaca"是不正确的，因为相同的字母必须放在一起。
#
#
# 示例 3:
#
#
# 输入:
# "Aabb"
#
# 输出:
# "bbAa"
#
# 解释:
# 此外，"bbaA"也是一个有效的答案，但"Aabb"是不正确的。
# 注意'A'和'a'被认为是两种不同的字符。
#
#
#
from collections import Counter

# from collections import defaultdict


# @lc code=start
class Solution:
    def frequencySort(self, s: str) -> str:
        return ''.join(ch * cnt for cnt, ch in Counter(s).most_common())


# @lc code=end

# class Solution:
#     def frequencySort(self, s: str) -> str:
#         counter = defaultdict(int)
#         for ch in s:
#             counter[ch] += 1

#         freq = [(cnt, ch) for ch, cnt in counter.items()]
#         freq.sort(reverse=True)
#         return ''.join(ch * cnt for cnt, ch in freq)

if __name__ == '__main__':
    solu = Solution()
    print(solu.frequencySort("tree"))
    print(solu.frequencySort("cccaaa"))
    print(solu.frequencySort("Aabb"))
