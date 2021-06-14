/*
 * @lc app=leetcode.cn id=374 lang=cpp
 *
 * [374] 猜数字大小
 *
 * https://leetcode-cn.com/problems/guess-number-higher-or-lower/description/
 *
 * algorithms
 * Easy (49.06%)
 * Likes:    133
 * Dislikes: 0
 * Total Accepted:    55.5K
 * Total Submissions: 113.3K
 * Testcase Example:  '10\n6'
 *
 * 猜数字游戏的规则如下：
 * 
 * 
 * 每轮游戏，我都会从 1 到 n 随机选择一个数字。 请你猜选出的是哪个数字。
 * 如果你猜错了，我会告诉你，你猜测的数字比我选出的数字是大了还是小了。
 * 
 * 
 * 你可以通过调用一个预先定义好的接口 int guess(int num) 来获取猜测结果，返回值一共有 3 种可能的情况（-1，1 或
 * 0）：
 * 
 * 
 * -1：我选出的数字比你猜的数字小 pick < num
 * 1：我选出的数字比你猜的数字大 pick > num
 * 0：我选出的数字和你猜的数字一样。恭喜！你猜对了！pick == num
 * 
 * 
 * 返回我选出的数字。
 * 
 * 
 * 
 * 示例 1：
 * 
 * 
 * 输入：n = 10, pick = 6
 * 输出：6
 * 
 * 
 * 示例 2：
 * 
 * 
 * 输入：n = 1, pick = 1
 * 输出：1
 * 
 * 
 * 示例 3：
 * 
 * 
 * 输入：n = 2, pick = 1
 * 输出：1
 * 
 * 
 * 示例 4：
 * 
 * 
 * 输入：n = 2, pick = 2
 * 输出：2
 * 
 * 
 * 
 * 
 * 提示：
 * 
 * 
 * 1 <= n <= 231 - 1
 * 1 <= pick <= n
 * 
 * 
 */

/**
 * @File    :   374.猜数字大小.cpp
 * @Time    :   2021/06/14 09:34:09
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 */

#include <bits/stdc++.h>
using namespace std;

/** 
 * Forward declaration of guess API.
 * @param  num   your guess
 * @return 	     -1 if num is lower than the guess number
 *			      1 if num is higher than the guess number
 *               otherwise return 0
 */
int guess(int num);

// @lc code=start
class Solution {
public:
    int guessNumber(int n) {
        int left = 1, right = n;
        while (left <= right) {
            int mid = left + (right - left) / 2;
            int res = guess(mid);
            if (res == 0) {
                return mid;
            } else if (res == 1) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        return left;
    }
};
// @lc code=end
