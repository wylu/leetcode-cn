/*
 * @lc app=leetcode.cn id=164 lang=cpp
 *
 * [164] 最大间距
 *
 * https://leetcode-cn.com/problems/maximum-gap/description/
 *
 * algorithms
 * Hard (55.18%)
 * Likes:    314
 * Dislikes: 0
 * Total Accepted:    42.7K
 * Total Submissions: 69.9K
 * Testcase Example:  '[3,6,9,1]'
 *
 * 给定一个无序的数组，找出数组在排序之后，相邻元素之间最大的差值。
 * 
 * 如果数组元素个数小于 2，则返回 0。
 * 
 * 示例 1:
 * 
 * 输入: [3,6,9,1]
 * 输出: 3
 * 解释: 排序后的数组是 [1,3,6,9], 其中相邻元素 (3,6) 和 (6,9) 之间都存在最大差值 3。
 * 
 * 示例 2:
 * 
 * 输入: [10]
 * 输出: 0
 * 解释: 数组元素个数小于 2，因此返回 0。
 * 
 * 说明:
 * 
 * 
 * 你可以假设数组中所有元素都是非负整数，且数值在 32 位有符号整数范围内。
 * 请尝试在线性时间复杂度和空间复杂度的条件下解决此问题。
 * 
 * 
 */

/**
 * @File    :   164.最大间距.cpp
 * @Time    :   2020/11/26 23:33:10
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
    int maximumGap(vector<int>& nums) {
        int n = nums.size();
        if (n < 2) return 0;

        int maxVal = *max_element(nums.begin(), nums.end());
        vector<int> buf(n);

        for (int exp = 1; exp <= maxVal; exp *= 10) {
            vector<int> cnt(10);
            for (int i = 0; i < n; i++) {
                int digit = nums[i] / exp % 10;
                cnt[digit]++;
            }

            for (int i = 1; i < 10; i++) {
                cnt[i] += cnt[i - 1];
            }

            for (int i = n - 1; i >= 0; i--) {
                int digit = nums[i] / exp % 10;
                buf[cnt[digit] - 1] = nums[i];
                cnt[digit]--;
            }

            copy(buf.begin(), buf.end(), nums.begin());
        }

        int ans = 0;
        for (int i = 1; i < n; i++) {
            ans = max(ans, nums[i] - nums[i - 1]);
        }

        return ans;
    }
};
// @lc code=end
