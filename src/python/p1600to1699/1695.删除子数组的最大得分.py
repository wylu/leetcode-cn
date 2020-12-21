#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   1695.删除子数组的最大得分.py
@Time    :   2020/12/21 11:26:52
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=1695 lang=python3
#
# [1695] 删除子数组的最大得分
#
# https://leetcode-cn.com/problems/maximum-erasure-value/description/
#
# algorithms
# Medium (39.65%)
# Likes:    11
# Dislikes: 0
# Total Accepted:    2.8K
# Total Submissions: 6.9K
# Testcase Example:  '[4,2,4,5,6]'
#
# 给你一个正整数数组 nums ，请你从中删除一个含有 若干不同元素 的子数组。删除子数组的 得分 就是子数组各元素之 和 。
#
# 返回 只删除一个 子数组可获得的 最大得分 。
#
# 如果数组 b 是数组 a 的一个连续子序列，即如果它等于 a[l],a[l+1],...,a[r] ，那么它就是 a 的一个子数组。
#
#
#
# 示例 1：
#
#
# 输入：nums = [4,2,4,5,6]
# 输出：17
# 解释：最优子数组是 [2,4,5,6]
#
#
# 示例 2：
#
#
# 输入：nums = [5,2,1,2,5,2,1,2,5]
# 输出：8
# 解释：最优子数组是 [5,2,1] 或 [1,2,5]
#
#
#
#
# 提示：
#
#
# 1 <= nums.length <= 10^5
# 1 <= nums[i] <= 10^4
#
#
#
from typing import List


# @lc code=start
class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        i, j, n = 0, 0, len(nums)
        ans, tot, seen = 0, 0, set()

        while i < n:
            while j < n and nums[j] not in seen:
                tot += nums[j]
                seen.add(nums[j])
                j += 1

            ans = max(ans, tot)
            tot -= nums[i]
            seen.remove(nums[i])
            i += 1

        return ans


# @lc code=end

if __name__ == "__main__":
    solu = Solution()
    print(solu.maximumUniqueSubarray([4, 2, 4, 5, 6]))
    print(solu.maximumUniqueSubarray([5, 2, 1, 2, 5, 2, 1, 2, 5]))
