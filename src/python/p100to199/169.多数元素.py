#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   169.多数元素.py
@Time    :   2020/09/03 22:19:43
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=169 lang=python3
#
# [169] 多数元素
#
# https://leetcode-cn.com/problems/majority-element/description/
#
# algorithms
# Easy (64.45%)
# Likes:    724
# Dislikes: 0
# Total Accepted:    208.9K
# Total Submissions: 324.2K
# Testcase Example:  '[3,2,3]'
#
# 给定一个大小为 n 的数组，找到其中的多数元素。多数元素是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。
#
# 你可以假设数组是非空的，并且给定的数组总是存在多数元素。
#
#
#
# 示例 1:
#
# 输入: [3,2,3]
# 输出: 3
#
# 示例 2:
#
# 输入: [2,2,1,1,1,2,2]
# 输出: 2
#
#
#
from typing import List
"""
Boyer-Moore 投票算法

思路

如果我们把众数记为 +1，把其他数记为 −1，将它们全部加起来，显然和大于 0，
从结果本身我们可以看出众数比其他数多。

算法

Boyer-Moore 算法的本质和分治十分类似。首先给出 Boyer-Moore 算法的详细步骤：

  - 维护一个候选众数 candidate 和它出现的次数 count。初始时 candidate
    可以为任意值，count 为 0；
  - 遍历数组 nums 中的所有元素，对于每个元素 x，在判断 x 之前，如果 count
    的值为 0，我们先将 x 的值赋予 candidate，随后我们判断 x：
    - 如果 x 与 candidate 相等，那么计数器 count 的值增加 1；
    - 如果 x 与 candidate 不等，那么计数器 count 的值减少 1。
  - 在遍历完成后，candidate 即为整个数组的众数。

举一个具体的例子，例如下面的这个数组：

nums:      [7, 7, 5, 7, 5, 1 | 5, 7 | 5, 5, 7, 7 | 7, 7, 7, 7]
candidate:  7  7  7  7  7  7   5  5   5  5  5  5   7  7  7  7
count:      1  2  1  2  1  0   1  0   1  2  1  0   1  2  3  4

在遍历到数组中的第一个元素以及每个在 | 之后的元素时，candidate 都会
因为 count 的值变为 0 而发生改变。最后一次 candidate 的值从 5 变为 7，
也就是这个数组中的众数。
"""


# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cnt, cdd = 0, None
        for num in nums:
            if cnt == 0:
                cdd = num
            cnt += 1 if cdd == num else -1
        return cdd


# @lc code=end

if __name__ == '__main__':
    solu = Solution()
    print(
        solu.majorityElement([7, 7, 5, 7, 5, 1, 5, 7, 5, 5, 7, 7, 7, 7, 7, 7]))
