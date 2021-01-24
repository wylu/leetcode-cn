#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   674.最长连续递增序列.py
@Time    :   2021/01/24 21:45:45
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=674 lang=python3
#
# [674] 最长连续递增序列
#
# https://leetcode-cn.com/problems/longest-continuous-increasing-subsequence/description/
#
# algorithms
# Easy (47.00%)
# Likes:    161
# Dislikes: 0
# Total Accepted:    60.5K
# Total Submissions: 128.7K
# Testcase Example:  '[1,3,5,4,7]'
#
# 给定一个未经排序的整数数组，找到最长且 连续递增的子序列，并返回该序列的长度。
#
# 连续递增的子序列 可以由两个下标 l 和 r（l < r）确定，如果对于每个 l ，都有 nums[i] < nums[i + 1] ，那么子序列
# [nums[l], nums[l + 1], ..., nums[r - 1], nums[r]] 就是连续递增子序列。
#
#
#
# 示例 1：
#
#
# 输入：nums = [1,3,5,4,7]
# 输出：3
# 解释：最长连续递增序列是 [1,3,5], 长度为3。
# 尽管 [1,3,5,7] 也是升序的子序列, 但它不是连续的，因为 5 和 7 在原数组里被 4 隔开。
#
#
# 示例 2：
#
#
# 输入：nums = [2,2,2,2,2]
# 输出：1
# 解释：最长连续递增序列是 [2], 长度为1。
#
#
#
#
# 提示：
#
#
# 0 <= nums.length <= 10^4
# -10^9 <= nums[i] <= 10^9
#
#
#
from typing import List


# @lc code=start
class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        ans, start = 0, 0
        for i in range(len(nums)):
            if i > 0 and nums[i] <= nums[i - 1]:
                start = i
            ans = max(ans, i - start + 1)
        return ans


# @lc code=end

if __name__ == "__main__":
    solu = Solution()
    print(solu.findLengthOfLCIS([1, 3, 5, 4, 7]))
    print(solu.findLengthOfLCIS([2, 2, 2, 2, 2]))
    print(solu.findLengthOfLCIS([]))
