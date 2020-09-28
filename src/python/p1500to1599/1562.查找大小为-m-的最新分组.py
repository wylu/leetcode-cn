#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   1562.查找大小为-m-的最新分组.py
@Time    :   2020/09/28 17:10:20
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=1562 lang=python3
#
# [1562] 查找大小为 M 的最新分组
#
# https://leetcode-cn.com/problems/find-latest-group-of-size-m/description/
#
# algorithms
# Medium (29.18%)
# Likes:    24
# Dislikes: 0
# Total Accepted:    3.3K
# Total Submissions: 11.4K
# Testcase Example:  '[3,5,1,2,4]\n1'
#
# 给你一个数组 arr ，该数组表示一个从 1 到 n 的数字排列。有一个长度为 n 的二进制字符串，该字符串上的所有位最初都设置为 0 。
#
# 在从 1 到 n 的每个步骤 i 中（假设二进制字符串和 arr 都是从 1 开始索引的情况下），二进制字符串上位于位置 arr[i] 的位将会设为 1
# 。
#
# 给你一个整数 m ，请你找出二进制字符串上存在长度为 m 的一组 1 的最后步骤。一组 1 是一个连续的、由 1 组成的子串，且左右两边不再有可以延伸的
# 1 。
#
# 返回存在长度 恰好 为 m 的 一组 1  的最后步骤。如果不存在这样的步骤，请返回 -1 。
#
#
#
# 示例 1：
#
# 输入：arr = [3,5,1,2,4], m = 1
# 输出：4
# 解释：
# 步骤 1："00100"，由 1 构成的组：["1"]
# 步骤 2："00101"，由 1 构成的组：["1", "1"]
# 步骤 3："10101"，由 1 构成的组：["1", "1", "1"]
# 步骤 4："11101"，由 1 构成的组：["111", "1"]
# 步骤 5："11111"，由 1 构成的组：["11111"]
# 存在长度为 1 的一组 1 的最后步骤是步骤 4 。
#
# 示例 2：
#
# 输入：arr = [3,1,5,4,2], m = 2
# 输出：-1
# 解释：
# 步骤 1："00100"，由 1 构成的组：["1"]
# 步骤 2："10100"，由 1 构成的组：["1", "1"]
# 步骤 3："10101"，由 1 构成的组：["1", "1", "1"]
# 步骤 4："10111"，由 1 构成的组：["1", "111"]
# 步骤 5："11111"，由 1 构成的组：["11111"]
# 不管是哪一步骤都无法形成长度为 2 的一组 1 。
#
#
# 示例 3：
#
# 输入：arr = [1], m = 1
# 输出：1
#
#
# 示例 4：
#
# 输入：arr = [2,1], m = 2
# 输出：2
#
#
#
#
# 提示：
#
#
# n == arr.length
# 1 <= n <= 10^5
# 1 <= arr[i] <= n
# arr 中的所有整数 互不相同
# 1 <= m <= arr.length
#
#
#
from typing import List
"""
方法一：模拟

思路与算法

首先，我们考虑维护一个与原数组等大的数组 endpoints，其中 endpoints[i]
表示数组中包含位置 i 的连续 1 的分组的起点和终点。如果 arr[i] 为 0，
则记起点和终点均为 −1。

例如，如果数组当前的取值为 [0, 1, 1, 1, 0, 1, 1]，则数组 endpoints
的取值为：

[(-1, -1), (2, 4), (2, 4), (2, 4), (-1, -1), (6, 7), (6,7)]

注意本题中数组下标是从 1 开始的。

起始时，数组 arr 的值都为 0。随后当进行每一步操作时，如果该步骤为将
arr[i] 的值设为 1，则有以下三种情况：

（1）如果 arr[i] 的左右两个相邻元素（如果有）的值均为 −1，则此时生成了
一个新的长度为 1 的分组；
（2）如果左右两个相邻元素（如果有）的之一的取值为 1，则此时会生成一个
新的分组，该分组取代了已有的某个分组，其长度为该已有分组的长度加 1；
（3）如果左右两个相邻元素的取值都为 1，则此时会将左右两个分组合并成一个
新的分组，新分组的长度为两个分组的长度之和再加上 1。同时，原本的两个
分组会随之消失。

在每种情况下，我们都会修改数组 endpoints。不过对于一个新生成的分组，
我们无需修改其中每个位置的取值：只需修改该分组左右端点处的取值即可。
这是因为，在进行每一步操作时，都不会在一个已有的分组内部做修改，
只会考虑已有分组的端点处的取值。

与此同时，我们也需要统计长度为 m 的分组数量。如果进行完第 i 次操作后，
长度为 m 的分组数量大于 0，则更新返回值为 i。遍历结束后，就能得到答案。
"""


# @lc code=start
class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        n = len(arr)
        es = [(-1, -1)] * (n + 1)
        ans, cnt = -1, 0

        for i in range(n):
            left = right = arr[i]

            if arr[i] > 1 and es[arr[i] - 1][0] != -1:
                left = es[arr[i] - 1][0]
                llen = es[arr[i] - 1][1] - es[arr[i] - 1][0] + 1
                if llen == m:
                    cnt -= 1

            if arr[i] < n and es[arr[i] + 1][1] != -1:
                right = es[arr[i] + 1][1]
                rlen = es[arr[i] + 1][1] - es[arr[i] + 1][0] + 1
                if rlen == m:
                    cnt -= 1

            nlen = right - left + 1
            if nlen == m:
                cnt += 1

            if cnt > 0:
                ans = i + 1

            es[left] = es[right] = (left, right)

        return ans


# @lc code=end

if __name__ == '__main__':
    solu = Solution()
    print(solu.findLatestStep([3, 5, 1, 2, 4], 1))
    print(solu.findLatestStep([3, 5, 1, 2, 4], 2))
    print(solu.findLatestStep([1], 1))
    print(solu.findLatestStep([2, 1], 2))
