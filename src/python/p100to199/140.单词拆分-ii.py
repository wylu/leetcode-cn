#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   140.单词拆分-ii.py
@Time    :   2020/11/01 22:20:13
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=140 lang=python3
#
# [140] 单词拆分 II
#
# https://leetcode-cn.com/problems/word-break-ii/description/
#
# algorithms
# Hard (42.44%)
# Likes:    331
# Dislikes: 0
# Total Accepted:    31.6K
# Total Submissions: 74.6K
# Testcase Example:  '"catsanddog"\n["cat","cats","and","sand","dog"]'
#
# 给定一个非空字符串 s 和一个包含非空单词列表的字典
# wordDict，在字符串中增加空格来构建一个句子，使得句子中所有的单词都在词典中。返回所有这些可能的句子。
#
# 说明：
#
#
# 分隔时可以重复使用字典中的单词。
# 你可以假设字典中没有重复的单词。
#
#
# 示例 1：
#
# 输入:
# s = "catsanddog"
# wordDict = ["cat", "cats", "and", "sand", "dog"]
# 输出:
# [
# "cats and dog",
# "cat sand dog"
# ]
#
#
# 示例 2：
#
# 输入:
# s = "pineapplepenapple"
# wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
# 输出:
# [
# "pine apple pen apple",
# "pineapple pen apple",
# "pine applepen apple"
# ]
# 解释: 注意你可以重复使用字典中的单词。
#
#
# 示例 3：
#
# 输入:
# s = "catsandog"
# wordDict = ["cats", "dog", "sand", "and", "cat"]
# 输出:
# []
#
#
#
from functools import lru_cache
from typing import List
"""
方法一：记忆化搜索

对于字符串 s，如果某个前缀是单词列表中的单词，则拆分出该单词，然后对 s 的剩余
部分继续拆分。如果可以将整个字符串 s 拆分成单词列表中的单词，则得到一个句子。
在对 s 的剩余部分拆分得到一个句子之后，将拆分出的第一个单词（即 s 的前缀）
添加到句子的头部，即可得到一个完整的句子。上述过程可以通过回溯实现。

假设字符串 s 的长度为 n，回溯的时间复杂度在最坏情况下高达 O(n^n)。时间复杂度
高的原因是存在大量重复计算，可以通过记忆化的方式降低时间复杂度。

具体做法是，使用哈希表存储字符串 s 的每个下标和从该下标开始的部分可以组成的
句子列表，在回溯过程中如果遇到已经访问过的下标，则可以直接从哈希表得到结果，
而不需要重复计算。如果到某个下标发现无法匹配，则哈希表中该下标对应的是空列表，
因此可以对不能拆分的情况进行剪枝优化。

还有一个可优化之处为使用哈希集合存储单词列表中的单词，这样在判断一个字符串
是否是单词列表中的单词时只需要判断该字符串是否在哈希集合中即可，而不再需要
遍历单词列表。
"""


# @lc code=start
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        n = len(s)

        @lru_cache(None)
        def backtrack(cur: int) -> List[List[str]]:
            if cur == n:
                return [[]]

            sts = []
            for i in range(cur + 1, n + 1):
                word = s[cur:i]
                if word in wordSet:
                    for sentence in backtrack(i):
                        sts.append([word] + sentence.copy())
            return sts

        wordSet = set(wordDict)
        return [' '.join(words) for words in backtrack(0)]


# @lc code=end
