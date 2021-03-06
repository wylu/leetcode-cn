#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   303.区域和检索-数组不可变.py
@Time    :   2021/03/01 22:02:43
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=303 lang=python3
#
# [303] 区域和检索 - 数组不可变
#
# https://leetcode-cn.com/problems/range-sum-query-immutable/description/
#
# algorithms
# Easy (70.02%)
# Likes:    291
# Dislikes: 0
# Total Accepted:    97.8K
# Total Submissions: 139.8K
# Testcase Example:
# '["NumArray","sumRange","sumRange","sumRange"]\n' +
# '[[[-2,0,3,-5,2,-1]],[0,2],[2,5],[0,5]]'
#
# 给定一个整数数组  nums，求出数组从索引 i 到 j（i ≤ j）范围内元素的总和，包含 i、j 两点。
#
#
#
# 实现 NumArray 类：
#
#
# NumArray(int[] nums) 使用数组 nums 初始化对象
# int sumRange(int i, int j) 返回数组 nums 从索引 i 到 j（i ≤ j）范围内元素的总和，包含 i、j 两点（也就是
# sum(nums[i], nums[i + 1], ... , nums[j])）
#
#
#
#
# 示例：
#
#
# 输入：
# ["NumArray", "sumRange", "sumRange", "sumRange"]
# [[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]
# 输出：
# [null, 1, -1, -3]
#
# 解释：
# NumArray numArray = new NumArray([-2, 0, 3, -5, 2, -1]);
# numArray.sumRange(0, 2); // return 1 ((-2) + 0 + 3)
# numArray.sumRange(2, 5); // return -1 (3 + (-5) + 2 + (-1))
# numArray.sumRange(0, 5); // return -3 ((-2) + 0 + 3 + (-5) + 2 + (-1))
#
#
#
#
# 提示：
#
#
# 0 <= nums.length <= 10^4
# -10^5 <= nums[i] <= 10^5
# 0 <= i <= j < nums.length
# 最多调用 10^4 次 sumRange 方法
#
#
#
#
#
from typing import List


# @lc code=start
class NumArray:
    def __init__(self, nums: List[int]):
        self.ps = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            self.ps[i + 1] = self.ps[i] + nums[i]

    def sumRange(self, i: int, j: int) -> int:
        return self.ps[j + 1] - self.ps[i]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
# @lc code=end
