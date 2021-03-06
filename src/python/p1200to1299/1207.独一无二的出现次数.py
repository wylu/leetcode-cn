#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   1207.独一无二的出现次数.py
@Time    :   2020/10/28 08:58:12
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=1207 lang=python3
#
# [1207] 独一无二的出现次数
#
# https://leetcode-cn.com/problems/unique-number-of-occurrences/description/
#
# algorithms
# Easy (71.43%)
# Likes:    57
# Dislikes: 0
# Total Accepted:    19.5K
# Total Submissions: 27.4K
# Testcase Example:  '[1,2,2,1,1,3]'
#
# 给你一个整数数组 arr，请你帮忙统计数组中每个数的出现次数。
#
# 如果每个数的出现次数都是独一无二的，就返回 true；否则返回 false。
#
#
#
# 示例 1：
#
# 输入：arr = [1,2,2,1,1,3]
# 输出：true
# 解释：在该数组中，1 出现了 3 次，2 出现了 2 次，3 只出现了 1 次。没有两个数的出现次数相同。
#
# 示例 2：
#
# 输入：arr = [1,2]
# 输出：false
#
#
# 示例 3：
#
# 输入：arr = [-3,0,1,-3,1,1,1,-3,10,0]
# 输出：true
#
#
#
#
# 提示：
#
#
# 1 <= arr.length <= 1000
# -1000 <= arr[i] <= 1000
#
#
#
from collections import defaultdict
from typing import List


# @lc code=start
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        cnt = defaultdict(int)
        for num in arr:
            cnt[num] += 1
        return len(cnt.values()) == len(set(cnt.values()))


# @lc code=end

if __name__ == "__main__":
    solu = Solution()
    print(solu.uniqueOccurrences([1, 2, 2, 1, 1, 3]))
    print(solu.uniqueOccurrences([1, 2]))
    print(solu.uniqueOccurrences([-3, 0, 1, -3, 1, 1, 1, -3, 10, 0]))
