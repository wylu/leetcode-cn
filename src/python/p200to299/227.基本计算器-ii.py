#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   227.基本计算器-ii.py
@Time    :   2021/03/11 22:44:19
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=227 lang=python3
#
# [227] 基本计算器 II
#
# https://leetcode-cn.com/problems/basic-calculator-ii/description/
#
# algorithms
# Medium (42.72%)
# Likes:    342
# Dislikes: 0
# Total Accepted:    56.5K
# Total Submissions: 132.4K
# Testcase Example:  '"3+2*2"'
#
# 给你一个字符串表达式 s ，请你实现一个基本计算器来计算并返回它的值。
#
# 整数除法仅保留整数部分。
#
#
#
#
#
# 示例 1：
#
#
# 输入：s = "3+2*2"
# 输出：7
#
#
# 示例 2：
#
#
# 输入：s = " 3/2 "
# 输出：1
#
#
# 示例 3：
#
#
# 输入：s = " 3+5 / 2 "
# 输出：5
#
#
#
#
# 提示：
#
#
# 1 <= s.length <= 3 * 10^5
# s 由整数和算符 ('+', '-', '*', '/') 组成，中间由一些空格隔开
# s 表示一个 有效表达式
# 表达式中的所有整数都是非负整数，且在范围 [0, 2^31 - 1] 内
# 题目数据保证答案是一个 32-bit 整数
#
#
#
#
#
"""
方法一：栈
思路

由于乘除优先于加减计算，因此不妨考虑先进行所有乘除运算，并将这些乘除
运算后的整数值放回原表达式的相应位置，则随后整个表达式的值，就等于
一系列整数加减后的值。

基于此，我们可以用一个栈，保存这些（进行乘除运算后的）整数的值。对于
加减号后的数字，将其直接压入栈中；对于乘除号后的数字，可以直接与栈顶
元素计算，并替换栈顶元素为计算后的结果。

具体来说，遍历字符串 s，并用变量 preSign 记录每个数字之前的运算符，
对于第一个数字，其之前的运算符视为加号。每次遍历到数字末尾时，根据
preSign 来决定计算方式：

  - 加号：将数字压入栈；
  - 减号：将数字的相反数压入栈；
  - 乘除号：计算数字与栈顶元素，并将栈顶元素替换为计算结果。

代码实现中，若读到一个运算符，或者遍历到字符串末尾，即认为是遍历到了
数字末尾。处理完该数字后，更新 preSign 为当前遍历的字符。

遍历完字符串 s 后，将栈中元素累加，即为该字符串表达式的值。
"""


# @lc code=start
class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        preSign = '+'
        num = 0
        n = len(s)

        for i in range(n):
            if '0' <= s[i] <= '9':
                num = num * 10 + ord(s[i]) - ord('0')

            if s[i] in '+-*/' or i == n - 1:
                if preSign == '+':
                    stack.append(num)
                elif preSign == '-':
                    stack.append(-num)
                elif preSign == '*':
                    stack.append(stack.pop() * num)
                else:
                    stack.append(int(stack.pop() / num))

                preSign = s[i]
                num = 0

        return sum(stack)


# @lc code=end

if __name__ == "__main__":
    solu = Solution()
    print(solu.calculate("3+2*2"))
    print(solu.calculate(" 3/2 "))
    print(solu.calculate(" 3+5 / 2 "))
    print(solu.calculate("14-3/2"))
