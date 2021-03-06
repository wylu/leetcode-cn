#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   1423.可获得的最大点数.py
@Time    :   2020/11/16 19:04:55
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=1423 lang=python3
#
# [1423] 可获得的最大点数
#
# https://leetcode-cn.com/problems/maximum-points-you-can-obtain-from-cards/description/
#
# algorithms
# Medium (43.74%)
# Likes:    31
# Dislikes: 0
# Total Accepted:    6.5K
# Total Submissions: 14.8K
# Testcase Example:  '[1,2,3,4,5,6,1]\n3'
#
# 几张卡牌 排成一行，每张卡牌都有一个对应的点数。点数由整数数组 cardPoints 给出。
#
# 每次行动，你可以从行的开头或者末尾拿一张卡牌，最终你必须正好拿 k 张卡牌。
#
# 你的点数就是你拿到手中的所有卡牌的点数之和。
#
# 给你一个整数数组 cardPoints 和整数 k，请你返回可以获得的最大点数。
#
#
#
# 示例 1：
#
# 输入：cardPoints = [1,2,3,4,5,6,1], k = 3
# 输出：12
# 解释：第一次行动，不管拿哪张牌，你的点数总是 1 。但是，先拿最右边的卡牌将会最大化你的可获得点数。最优策略是拿右边的三张牌，最终点数为 1 + 6 +
# 5 = 12 。
#
#
# 示例 2：
#
# 输入：cardPoints = [2,2,2], k = 2
# 输出：4
# 解释：无论你拿起哪两张卡牌，可获得的点数总是 4 。
#
#
# 示例 3：
#
# 输入：cardPoints = [9,7,7,9,7,7,9], k = 7
# 输出：55
# 解释：你必须拿起所有卡牌，可以获得的点数为所有卡牌的点数之和。
#
#
# 示例 4：
#
# 输入：cardPoints = [1,1000,1], k = 1
# 输出：1
# 解释：你无法拿到中间那张卡牌，所以可以获得的最大点数为 1 。
#
#
# 示例 5：
#
# 输入：cardPoints = [1,79,80,1,1,1,200,1], k = 3
# 输出：202
#
#
#
#
# 提示：
#
#
# 1 <= cardPoints.length <= 10^5
# 1 <= cardPoints[i] <= 10^4
# 1 <= k <= cardPoints.length
#
#
#
from typing import List
"""
方法一：滑动窗口
思路

记数组 cardPoints 的长度为 n，由于只能从开头和末尾拿 k 张卡牌，所以最后
剩下的必然是连续的 n-k 张卡牌。

我们可以通过求出剩余卡牌点数之和的最小值，来求出拿走卡牌点数之和的最大值。

算法

由于剩余卡牌是连续的，使用一个固定长度为 n-k 的滑动窗口对数组 cardPoints
进行遍历，求出滑动窗口最小值，然后用所有卡牌的点数之和减去该最小值，即得
到了拿走卡牌点数之和的最大值。
"""


# @lc code=start
class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        r = n - k
        ans = tot = sum(cardPoints[:r])
        for i in range(1, n - r + 1):
            tot = tot - cardPoints[i - 1] + cardPoints[i + r - 1]
            ans = min(ans, tot)
        return sum(cardPoints) - ans


# @lc code=end

if __name__ == "__main__":
    solu = Solution()
    print(solu.maxScore([1, 2, 3, 4, 5, 6, 1], 3))
    print(solu.maxScore([2, 2, 2], 2))
    print(solu.maxScore([9, 7, 7, 9, 7, 7, 9], 7))
    print(solu.maxScore([1, 1000, 1], 1))
    print(solu.maxScore([1, 79, 80, 1, 1, 1, 200, 1], 3))
    print(solu.maxScore([96, 90, 41, 82, 39, 74, 64, 50, 30], 8))
