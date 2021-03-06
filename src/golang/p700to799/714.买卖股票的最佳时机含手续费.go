package p700to799

/*
 * @lc app=leetcode.cn id=714 lang=golang
 *
 * [714] 买卖股票的最佳时机含手续费
 *
 * https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/description/
 *
 * algorithms
 * Medium (66.01%)
 * Likes:    205
 * Dislikes: 0
 * Total Accepted:    23.2K
 * Total Submissions: 34.9K
 * Testcase Example:  '[1,3,2,8,4,9]\n2'
 *
 * 给定一个整数数组 prices，其中第 i 个元素代表了第 i 天的股票价格 ；非负整数 fee 代表了交易股票的手续费用。
 *
 * 你可以无限次地完成交易，但是你每笔交易都需要付手续费。如果你已经购买了一个股票，在卖出它之前你就不能再继续购买股票了。
 *
 * 返回获得利润的最大值。
 *
 * 注意：这里的一笔交易指买入持有并卖出股票的整个过程，每笔交易你只需要为支付一次手续费。
 *
 * 示例 1:
 *
 * 输入: prices = [1, 3, 2, 8, 4, 9], fee = 2
 * 输出: 8
 * 解释: 能够达到的最大利润:
 * 在此处买入 prices[0] = 1
 * 在此处卖出 prices[3] = 8
 * 在此处买入 prices[4] = 4
 * 在此处卖出 prices[5] = 9
 * 总利润: ((8 - 1) - 2) + ((9 - 4) - 2) = 8.
 *
 * 注意:
 *
 *
 * 0 < prices.length <= 50000.
 * 0 < prices[i] < 50000.
 * 0 <= fee < 50000.
 *
 *
 */

/**
 * @File    :   714.买卖股票的最佳时机含手续费.go
 * @Time    :   2020/07/11 18:10:49
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 *
 * https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/discuss/108870/Most-consistent-ways-of-dealing-with-the-series-of-stock-problems
 *
 * Dynamic Programming
 *
 * State:
 *   dp[i][0]: 表示第 i+1 天结束时，不持有股票，所能获得的最大利润。
 *   dp[i][1]: 表示第 i+1 天结束时，持有股票，所能获得的最大利润。
 *
 * Initial State:
 *   dp[0][0] = 0
 *   dp[0][1] = -prices[0]
 *
 * State Transition:
 *   dp[i][0] = max(dp[i-1][0], dp[i-1][1]+prices[i]-fee), i > 0
 *   dp[i][1] = max(dp[i-1][1], dp[i-1][0]-prices[i]), i > 0
 */
// @lc code=start
func maxProfit(prices []int, fee int) int {
	max := func(x, y int) int {
		if x > y {
			return x
		}
		return y
	}

	dp0, dp1 := 0, -prices[0]
	for i := 1; i < len(prices); i++ {
		dp0 = max(dp0, dp1+prices[i]-fee)
		dp1 = max(dp1, dp0-prices[i])
	}
	return dp0
}

// @lc code=end
