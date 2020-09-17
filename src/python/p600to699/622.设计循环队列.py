#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   622.设计循环队列.py
@Time    :   2020/09/17 23:28:43
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=622 lang=python3
#
# [622] 设计循环队列
#
# https://leetcode-cn.com/problems/design-circular-queue/description/
#
# algorithms
# Medium (41.43%)
# Likes:    140
# Dislikes: 0
# Total Accepted:    39K
# Total Submissions: 94K
# Testcase Example:
# '["MyCircularQueue","enQueue","enQueue","enQueue","enQueue","Rear","isFull","deQueue","enQueue","Rear"]\n'
# + '[[3],[1],[2],[3],[4],[],[],[],[4],[]]'
#
# 设计你的循环队列实现。 循环队列是一种线性数据结构，其操作表现基于
# FIFO（先进先出）原则并且队尾被连接在队首之后以形成一个循环。它也被称为“环形缓冲器”。
#
#
# 循环队列的一个好处是我们可以利用这个队列之前用过的空间。在一个普通队列里，一旦一个队列满了，我们就不能插入下一个元素，即使在队列前面仍有空间。但是使用循环队列，我们能使用这些空间去存储新的值。
#
# 你的实现应该支持如下操作：
#
#
# MyCircularQueue(k): 构造器，设置队列长度为 k 。
# Front: 从队首获取元素。如果队列为空，返回 -1 。
# Rear: 获取队尾元素。如果队列为空，返回 -1 。
# enQueue(value): 向循环队列插入一个元素。如果成功插入则返回真。
# deQueue(): 从循环队列中删除一个元素。如果成功删除则返回真。
# isEmpty(): 检查循环队列是否为空。
# isFull(): 检查循环队列是否已满。
#
#
#
#
# 示例：
#
# MyCircularQueue circularQueue = new MyCircularQueue(3); // 设置长度为 3
# circularQueue.enQueue(1);  // 返回 true
# circularQueue.enQueue(2);  // 返回 true
# circularQueue.enQueue(3);  // 返回 true
# circularQueue.enQueue(4);  // 返回 false，队列已满
# circularQueue.Rear();  // 返回 3
# circularQueue.isFull();  // 返回 true
# circularQueue.deQueue();  // 返回 true
# circularQueue.enQueue(4);  // 返回 true
# circularQueue.Rear();  // 返回 4
#
#
#
# 提示：
#
#
# 所有的值都在 0 至 1000 的范围内；
# 操作数将在 1 至 1000 的范围内；
# 请不要使用内置的队列库。
#
#
#


# @lc code=start
class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class MyCircularQueue:
    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the queue
        to be k.
        """
        self.capacity = k
        self.head = None
        self.tail = None
        self.length = 0

    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the
        operation is successful.
        """
        if self.length == self.capacity:
            return False

        if self.length == 0:
            self.head = Node(value)
            self.tail = self.head
        else:
            node = Node(value)
            self.tail.next = node
            self.tail = node

        self.length += 1
        return True

    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue. Return true if the
        operation is successful.
        """
        if self.length == 0:
            return False

        self.head = self.head.next
        self.length -= 1
        return True

    def Front(self) -> int:
        """
        Get the front item from the queue.
        """
        if self.length == 0:
            return -1
        return self.head.val

    def Rear(self) -> int:
        """
        Get the last item from the queue.
        """
        if self.length == 0:
            return -1
        return self.tail.val

    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        return self.length == 0

    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """
        return self.length == self.capacity


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
# @lc code=end
