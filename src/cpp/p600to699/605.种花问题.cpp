/*
 * @lc app=leetcode.cn id=605 lang=cpp
 *
 * [605] 种花问题
 *
 * https://leetcode-cn.com/problems/can-place-flowers/description/
 *
 * algorithms
 * Easy (32.45%)
 * Likes:    223
 * Dislikes: 0
 * Total Accepted:    47.9K
 * Total Submissions: 147.7K
 * Testcase Example:  '[1,0,0,0,1]\n1'
 *
 * 假设你有一个很长的花坛，一部分地块种植了花，另一部分却没有。可是，花卉不能种植在相邻的地块上，它们会争夺水源，两者都会死去。
 * 
 * 给定一个花坛（表示为一个数组包含0和1，其中0表示没种植花，1表示种植了花），和一个数 n 。能否在不打破种植规则的情况下种入 n
 * 朵花？能则返回True，不能则返回False。
 * 
 * 示例 1:
 * 
 * 
 * 输入: flowerbed = [1,0,0,0,1], n = 1
 * 输出: True
 * 
 * 
 * 示例 2:
 * 
 * 
 * 输入: flowerbed = [1,0,0,0,1], n = 2
 * 输出: False
 * 
 * 
 * 注意:
 * 
 * 
 * 数组内已种好的花不会违反种植规则。
 * 输入的数组长度范围为 [1, 20000]。
 * n 是非负整数，且不会超过输入数组的大小。
 * 
 * 
 */

/**
 * @File    :   605.种花问题.cpp
 * @Time    :   2021/01/01 09:20:53
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 */

#include <bits/stdc++.h>
using namespace std;

// @lc code=start
class Solution {
public:
    bool canPlaceFlowers(vector<int>& flowerbed, int n) {
        int i = 0, m = flowerbed.size();

        while (n && i < m) {
            if (flowerbed[i]) {
                i += 2;
            } else if (i < m - 1 && flowerbed[i + 1]) {
                i += 3;
            } else {
                i += 2, n--;
            }
        }

        return n == 0;
    }
};
// @lc code=end
