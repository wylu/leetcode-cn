#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   901.股票价格跨度.py
@Time    :   2020/07/29 00:30:41
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=901 lang=python3
#
# [901] 股票价格跨度
#
# https://leetcode-cn.com/problems/online-stock-span/description/
#
# algorithms
# Medium (45.85%)
# Likes:    55
# Dislikes: 0
# Total Accepted:    6.5K
# Total Submissions: 14.1K
# Testcase Example:
# '["StockSpanner","next","next","next","next","next","next","next"]\n' +
# '[[],[100],[80],[60],[70],[60],[75],[85]]'
#
# 编写一个 StockSpanner 类，它收集某些股票的每日报价，并返回该股票当日价格的跨度。
#
# 今天股票价格的跨度被定义为股票价格小于或等于今天价格的最大连续日数（从今天开始往回数，包括今天）。
#
# 例如，如果未来7天股票的价格是 [100, 80, 60, 70, 60, 75, 85]，那么股票跨度将是
# [1, 1, 1, 2, 1, 4, 6]。
#
#
#
# 示例：
#
# 输入：["StockSpanner","next","next","next","next","next","next","next"],
# [[],[100],[80],[60],[70],[60],[75],[85]]
# 输出：[null,1,1,1,2,1,4,6]
# 解释：
# 首先，初始化 S = StockSpanner()，然后：
# S.next(100) 被调用并返回 1，
# S.next(80) 被调用并返回 1，
# S.next(60) 被调用并返回 1，
# S.next(70) 被调用并返回 2，
# S.next(60) 被调用并返回 1，
# S.next(75) 被调用并返回 4，
# S.next(85) 被调用并返回 6。
#
# 注意 (例如) S.next(75) 返回 4，因为截至今天的最后 4 个价格
# (包括今天的价格 75) 小于或等于今天的价格。
#
#
#
#
# 提示：
#
#
# 调用 StockSpanner.next(int price) 时，将有 1 <= price <= 10^5。
# 每个测试用例最多可以调用  10000 次 StockSpanner.next。
# 在所有测试用例中，最多调用 150000 次 StockSpanner.next。
# 此问题的总时间限制减少了 50%。
#
#
#
"""
单调栈

求出小于或等于今天价格的最大连续日数等价于求出最近的一个大于今日价格的日子。
如果第 i 天的价格为 A[i]，第 j 天的价格为 A[j]，满足 i < j 且 A[i] <= A[j]，
那么在第 j 天之后，第 i 天不会是任何一天询问的答案，因为如果对于第 k, k > j
天而言，第 i 天是最近的一个大于今日价格的日子，但第 j 天出现在第 i 天之后且
价格不低于第 i 天，因此出现了矛盾。

有了这样一个结论，我们只需要维护一个单调递减的序列，称之为单调栈。例如股票每天
的价格为 [11, 3, 9, 5, 6, 4]，那么每天结束之后，对应的单调栈分别为：

[11]
[11, 3]
[11, 9]
[11, 9, 5]
[11, 9, 6]
[11, 9, 6, 4]

当我们得到了新的一天的价格（例如 7）时，我们将栈中所有小于等于 7 的元素全部取出，
因为根据之前的结论，这些元素不会成为后续询问的答案。当栈顶的元素大于 7 时，我们
就得到最近的一个大于 7 的价格为 9。

算法

我们用单调栈维护一个单调递减的价格序列，并且对于每个价格，存储一个 weight 表示
它离上一个价格之间（即最近的一个大于它的价格之间）的天数。如果是栈底的价格，则
存储它本身对应的天数。例如 [11, 3, 9, 5, 6, 4, 7] 对应的单调栈为
(11, weight=1), (9, weight=2), (7, weight=4)。

当我们得到了新的一天的价格，例如 10，我们将所有栈中所有小于等于 10 的元素全部取出，
将它们的 weight 进行累加，再加上 1 就得到了答案。在这之后，我们把 10 和它对应的
weight 放入栈中，得到 (11, weight=1), (10, weight=7)。
"""


# @lc code=start
class StockSpanner:
    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        weight = 1
        while self.stack and self.stack[-1][0] <= price:
            weight += self.stack.pop()[1]
        self.stack.append((price, weight))
        return weight


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
# @lc code=end
