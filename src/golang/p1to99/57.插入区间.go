package p1to99

/*
 * @lc app=leetcode.cn id=57 lang=golang
 *
 * [57] 插入区间
 *
 * https://leetcode-cn.com/problems/insert-interval/description/
 *
 * algorithms
 * Hard (38.03%)
 * Likes:    235
 * Dislikes: 0
 * Total Accepted:    34.6K
 * Total Submissions: 89.8K
 * Testcase Example:  '[[1,3],[6,9]]\n[2,5]'
 *
 * 给出一个无重叠的 ，按照区间起始端点排序的区间列表。
 *
 * 在列表中插入一个新的区间，你需要确保列表中的区间仍然有序且不重叠（如果有必要的话，可以合并区间）。
 *
 *
 *
 * 示例 1：
 *
 * 输入：intervals = [[1,3],[6,9]], newInterval = [2,5]
 * 输出：[[1,5],[6,9]]
 *
 *
 * 示例 2：
 *
 * 输入：intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
 * 输出：[[1,2],[3,10],[12,16]]
 * 解释：这是因为新的区间 [4,8] 与 [3,5],[6,7],[8,10] 重叠。
 *
 *
 *
 *
 * 注意：输入类型已在 2019 年 4 月 15 日更改。请重置为默认代码定义以获取新的方法签名。
 *
 */

/**
 * @File    :   57.插入区间.go
 * @Time    :   2020/11/04 10:16:05
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 */

// @lc code=start
func insert(intervals [][]int, nitv []int) [][]int {
	placed := false
	ans := [][]int{}

	max := func(x, y int) int {
		if x > y {
			return x
		}
		return y
	}

	min := func(x, y int) int {
		if x < y {
			return x
		}
		return y
	}

	for _, itv := range intervals {
		if itv[0] > nitv[1] {
			// 在插入区间的右侧且无交集
			if !placed {
				ans = append(ans, []int{nitv[0], nitv[1]})
				placed = true
			}
			ans = append(ans, itv)
		} else if itv[1] < nitv[0] {
			// 在插入区间的左侧且无交集
			ans = append(ans, itv)
		} else {
			// 与插入区间有交集，计算它们的并集
			nitv[0] = min(nitv[0], itv[0])
			nitv[1] = max(nitv[1], itv[1])
		}
	}

	if !placed {
		ans = append(ans, nitv)
	}

	return ans
}

// @lc code=end
