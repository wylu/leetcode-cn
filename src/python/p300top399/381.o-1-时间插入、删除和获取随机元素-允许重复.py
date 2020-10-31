#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   381.o-1-时间插入、删除和获取随机元素-允许重复.py
@Time    :   2020/10/31 11:34:12
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=381 lang=python3
#
# [381] O(1) 时间插入、删除和获取随机元素 - 允许重复
#
# https://leetcode-cn.com/problems/insert-delete-getrandom-o1-duplicates-allowed/description/
#
# algorithms
# Hard (38.05%)
# Likes:    126
# Dislikes: 0
# Total Accepted:    8.2K
# Total Submissions: 19.3K
# Testcase Example:
# '["RandomizedCollection","insert","insert","insert","getRandom","remove","getRandom"]\n'
# + '[[],[1],[1],[2],[],[1],[]]'
#
# 设计一个支持在平均 时间复杂度 O(1) 下， 执行以下操作的数据结构。
#
# 注意: 允许出现重复元素。
#
#
# insert(val)：向集合中插入元素 val。
# remove(val)：当 val 存在时，从集合中移除一个 val。
# getRandom：从现有集合中随机获取一个元素。每个元素被返回的概率应该与其在集合中的数量呈线性相关。
#
#
# 示例:
#
# // 初始化一个空的集合。
# RandomizedCollection collection = new RandomizedCollection();
#
# // 向集合中插入 1 。返回 true 表示集合不包含 1 。
# collection.insert(1);
#
# // 向集合中插入另一个 1 。返回 false 表示集合包含 1 。集合现在包含 [1,1] 。
# collection.insert(1);
#
# // 向集合中插入 2 ，返回 true 。集合现在包含 [1,1,2] 。
# collection.insert(2);
#
# // getRandom 应当有 2/3 的概率返回 1 ，1/3 的概率返回 2 。
# collection.getRandom();
#
# // 从集合中删除 1 ，返回 true 。集合现在包含 [1,2] 。
# collection.remove(1);
#
# // getRandom 应有相同概率返回 1 和 2 。
# collection.getRandom();
#
#
#
import random
from collections import defaultdict


# @lc code=start
class RandomizedCollection:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.idx = defaultdict(set)
        self.nums = []

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the collection.
        Returns true if the collection did not already contain the
        specified element.
        """
        self.nums.append(val)
        ans = not bool(self.idx[val])
        self.idx[val].add(len(self.nums) - 1)
        return ans

    def remove(self, val: int) -> bool:
        """
        Removes a value from the collection.
        Returns true if the collection contained the specified element.
        """
        if not self.idx[val]:
            return False

        i = self.idx[val].pop()
        j = len(self.nums) - 1
        if i != j:
            self.nums[i] = self.nums[j]
            self.idx[self.nums[i]].remove(j)
            self.idx[self.nums[i]].add(i)

        self.nums.pop()
        return True

    def getRandom(self) -> int:
        """
        Get a random element from the collection.
        """
        return self.nums[random.randrange(0, len(self.nums))]


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
# @lc code=end

if __name__ == "__main__":
    # Case 1
    rc = RandomizedCollection()
    print(rc.insert(1))
    print(rc.insert(1))
    print(rc.insert(2))
    print(rc.getRandom())
    print(rc.remove(1))
    print(rc.getRandom())
    print()

    # Case 2
    rc = RandomizedCollection()
    print(rc.insert(1))
    print(rc.remove(1))
    print(rc.insert(1))
