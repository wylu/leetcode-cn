package p500to599

/*
 * @lc app=leetcode.cn id=503 lang=golang
 *
 * [503] 下一个更大元素 II
 *
 * https://leetcode-cn.com/problems/next-greater-element-ii/description/
 *
 * algorithms
 * Medium (57.36%)
 * Likes:    186
 * Dislikes: 0
 * Total Accepted:    30.1K
 * Total Submissions: 52.5K
 * Testcase Example:  '[1,2,1]'
 *
 * 给定一个循环数组（最后一个元素的下一个元素是数组的第一个元素），输出每个元素的下一个更大元素。数字 x
 * 的下一个更大的元素是按数组遍历顺序，这个数字之后的第一个比它更大的数，这意味着你应该循环地搜索它的下一个更大的数。如果不存在，则输出 -1。
 *
 * 示例 1:
 *
 *
 * 输入: [1,2,1]
 * 输出: [2,-1,2]
 * 解释: 第一个 1 的下一个更大的数是 2；
 * 数字 2 找不到下一个更大的数；
 * 第二个 1 的下一个最大的数需要循环搜索，结果也是 2。
 *
 *
 * 注意: 输入数组的长度不会超过 10000。
 *
 */

/**
 * @File    :   503.下一个更大元素-ii.go
 * @Time    :   2020/09/15 00:10:56
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 */

// @lc code=start
func nextGreaterElements(nums []int) []int {
	n := len(nums)
	if n == 0 {
		return []int{}
	}

	ans := make([]int, n)
	for i := 0; i < n; i++ {
		ans[i] = -1
	}

	stack := []int{}
	for i := 0; i < n*2; i++ {
		m := len(stack)
		for m > 0 && nums[i%n] > nums[stack[m-1]] {
			ans[stack[m-1]] = nums[i%n]
			stack = stack[:m-1]
			m--
		}
		stack = append(stack, i%n)
	}

	return ans
}

// @lc code=end
