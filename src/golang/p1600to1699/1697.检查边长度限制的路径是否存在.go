package p1600to1699

import (
	"sort"
)

/*
 * @lc app=leetcode.cn id=1697 lang=golang
 *
 * [1697] 检查边长度限制的路径是否存在
 *
 * https://leetcode-cn.com/problems/checking-existence-of-edge-length-limited-paths/description/
 *
 * algorithms
 * Hard (40.57%)
 * Likes:    17
 * Dislikes: 0
 * Total Accepted:    844
 * Total Submissions: 2.1K
 * Testcase Example:  '3\n[[0,1,2],[1,2,4],[2,0,8],[1,0,16]]\n[[0,1,2],[0,2,5]]'
 *
 * 给你一个 n 个点组成的无向图边集 edgeList ，其中 edgeList[i] = [ui, vi, disi] 表示点 ui 和点 vi
 * 之间有一条长度为 disi 的边。请注意，两个点之间可能有 超过一条边 。
 *
 * 给你一个查询数组queries ，其中 queries[j] = [pj, qj, limitj] ，你的任务是对于每个查询 queries[j]
 * ，判断是否存在从 pj 到 qj 的路径，且这条路径上的每一条边都 严格小于 limitj 。
 *
 * 请你返回一个 布尔数组 answer ，其中 answer.length == queries.length ，当 queries[j] 的查询结果为
 * true 时， answer 第 j 个值为 true ，否则为 false 。
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：n = 3, edgeList = [[0,1,2],[1,2,4],[2,0,8],[1,0,16]], queries =
 * [[0,1,2],[0,2,5]]
 * 输出：[false,true]
 * 解释：上图为给定的输入数据。注意到 0 和 1 之间有两条重边，分别为 2 和 16 。
 * 对于第一个查询，0 和 1 之间没有小于 2 的边，所以我们返回 false 。
 * 对于第二个查询，有一条路径（0 -> 1 -> 2）两条边都小于 5 ，所以这个查询我们返回 true 。
 *
 *
 * 示例 2：
 *
 *
 * 输入：n = 5, edgeList = [[0,1,10],[1,2,5],[2,3,9],[3,4,13]], queries =
 * [[0,4,14],[1,4,13]]
 * 输出：[true,false]
 * 解释：上图为给定数据。
 *
 *
 *
 *
 * 提示：
 *
 *
 * 2 <= n <= 10^5
 * 1 <= edgeList.length, queries.length <= 10^5
 * edgeList[i].length == 3
 * queries[j].length == 3
 * 0 <= ui, vi, pj, qj <= n - 1
 * ui != vi
 * pj != qj
 * 1 <= disi, limitj <= 10^9
 * 两个点之间可能有 多条 边。
 *
 *
 */

/**
 * @File    :   1697.检查边长度限制的路径是否存在.go
 * @Time    :   2020/12/22 10:24:59
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 * 方法一：并查集 + 离线处理
 *
 * 我们将 queries 按照 limit[j] 从小到大进行排序，这样所有的询问中对边权
 * 的限制就单调递增了。
 *
 * 同时，我们将 edgeList 按照 dis[i] 从小到大进行排序，这样所有的边权
 * 也就单调递增了。
 *
 * 此时我们就可以愉快地处理所有的询问了。我们使用并查集维护图的连通性，
 * 并且使用指针 i 表示当前往并查集中添加的最后一条边。当我们处理到询问
 * queries[j] = (p[j], q[j], limit[j]) 时，由于 limit[j] 是单调递增的，
 * 因此我们只需要往并查集中添加新的边，即不断地在 edgeList 中向右移动指针
 * i，直到当前指向的边权 dis[i] >= limit[j] 为止。随后我们只需要使用
 * 并查集判断 p[j] 和 q[j] 是否连通即可。
 *
 * 将 queries 和 edgeList 进行排序的巧妙之处就在于，我们实际上做了这样
 * 的一个操作：
 *   - 我们将所有的 queries 和 edgeList 合并在一起，并且按照边权或者边权
 *     限制进行排序。在出现相等的情况时，queries 或者 edgeList 内部的
 *     相对顺序并不重要，但所有的 queries 必须要排在所有的 edgeList 之前，
 *     这是因为题目中要求对于每一个询问，可以经过的边权是严格小于边权限制的；
 *   - 在排序之后，我们依次遍历所有的元素。如果当前元素是 queries，我们就
 *     使用并查集进行查询（询问两个点是否连通）操作；如果当前元素是
 *     edgeList，我们就是用并查集进行修改（添加一条边）操作。
 */

// @lc code=start

// UnionFind ...
type UnionFind struct {
	par []int
}

// NewUnionFind ...
func NewUnionFind(n int) *UnionFind {
	uf := UnionFind{par: make([]int, n)}
	for i := 0; i < n; i++ {
		uf.par[i] = i
	}
	return &uf
}

// Find ...
func (uf *UnionFind) Find(x int) int {
	if uf.par[x] != x {
		uf.par[x] = uf.Find(uf.par[x])
	}
	return uf.par[x]
}

// Union ...
func (uf *UnionFind) Union(x, y int) {
	uf.par[uf.Find(x)] = uf.Find(y)
}

// Connected ...
func (uf *UnionFind) Connected(x, y int) bool {
	return uf.Find(x) == uf.Find(y)
}

func distanceLimitedPathsExist(n int, edgeList [][]int, queries [][]int) []bool {
	m := len(queries)
	indices := make([]int, m)
	for i := 0; i < m; i++ {
		indices[i] = i
	}
	sort.Slice(indices, func(i, j int) bool {
		return queries[indices[i]][2] < queries[indices[j]][2]
	})
	sort.Slice(edgeList, func(i, j int) bool {
		return edgeList[i][2] < edgeList[j][2]
	})

	ans := make([]bool, m)
	uf := NewUnionFind(n)
	i, el := 0, len(edgeList)
	for _, j := range indices {
		for i < el && edgeList[i][2] < queries[j][2] {
			uf.Union(edgeList[i][0], edgeList[i][1])
			i++
		}
		ans[j] = uf.Connected(queries[j][0], queries[j][1])
	}

	return ans
}

// @lc code=end
