#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   959.由斜杠划分区域.py
@Time    :   2021/01/25 13:50:45
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=959 lang=python3
#
# [959] 由斜杠划分区域
#
# https://leetcode-cn.com/problems/regions-cut-by-slashes/description/
#
# algorithms
# Medium (74.48%)
# Likes:    172
# Dislikes: 0
# Total Accepted:    9.5K
# Total Submissions: 12.7K
# Testcase Example:  '[" /","/ "]'
#
# 在由 1 x 1 方格组成的 N x N 网格 grid 中，每个 1 x 1 方块由 /、\ 或空格构成。这些字符会将方块划分为一些共边的区域。
#
# （请注意，反斜杠字符是转义的，因此 \ 用 "\\" 表示。）。
#
# 返回区域的数目。
#
#
#
#
#
#
# 示例 1：
#
# 输入：
# [
# " /",
# "/ "
# ]
# 输出：2
# 解释：2x2 网格如下：
#
#
# 示例 2：
#
# 输入：
# [
# " /",
# "  "
# ]
# 输出：1
# 解释：2x2 网格如下：
#
#
# 示例 3：
#
# 输入：
# [
# "\\/",
# "/\\"
# ]
# 输出：4
# 解释：（回想一下，因为 \ 字符是转义的，所以 "\\/" 表示 \/，而 "/\\" 表示 /\。）
# 2x2 网格如下：
#
#
# 示例 4：
#
# 输入：
# [
# "/\\",
# "\\/"
# ]
# 输出：5
# 解释：（回想一下，因为 \ 字符是转义的，所以 "/\\" 表示 /\，而 "\\/" 表示 \/。）
# 2x2 网格如下：
#
#
# 示例 5：
#
# 输入：
# [
# "//",
# "/ "
# ]
# 输出：3
# 解释：2x2 网格如下：
#
#
#
#
#
# 提示：
#
#
# 1 <= grid.length == grid[0].length <= 30
# grid[i][j] 是 '/'、'\'、或 ' '。
#
#
#
from typing import List
"""
方法一：并查集
我们沿着一个网格的两条对角线，能够将正方形切分成四个三角形。如果网格
上的字符为 /，则右下角的两个三角形会与左上角的两个三角形分隔开；同理，
如果字符为 \，则右上角的两个三角形会和左下角的两个三角形分隔开。

不难发现，如果将每个三角形看作为一张图上的节点，则网格中的一个共边
区域，就相当于图中的一个连通分量。因此，不难想到利用并查集求解连通
分量的数目。

设网格为 n * n 大小，则图中有 4 * n * n 个节点，每个格子对应其中
的 4 个节点。对于每个格子而言，考虑当前位置的字符：
  - 如果为空格，则该格子对应的 4 个节点应当同属于同一区域，因此在
    它们之间各连接一条边；
  - 如果为字符 /，则将左上角的两个格子连接一条边，并将右下角的两个
    格子连接一条边；
  - 如果为字符 \，则将右上角的两个格子连接一条边，并将左下角的两个
    格子连接一条边。

到目前位置，我们只考虑了一个格子内部的情况。但同时，不难观察到下面
两点：
  - 一个格子中最下方的三角形，必然和下面的格子（如果存在）中最上方
    的三角形连通；
  - 一个格子中最右方的三角形，必然和右边的格子（如果存在）中最左方
    的三角形连通。

因此，我们还需要根据上面两条规则，在相邻格子的相应三角形中间，再连接边。

最终，在构造出图后，利用并查集就可以求出连通分量的数目了。

具体实现方面，每个格子的 4 个节点按照上、右、下、左的顺序依次编号
0、1、2、3，每个节点可以根据格子所在的行和列以及节点在格子中的编号
唯一地确定。
"""


# @lc code=start
class UnionFind:
    def __init__(self, n: int):
        self.par = list(range(n))
        self.cnt = n

    def find(self, x: int) -> int:
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]

    def union(self, x: int, y: int) -> None:
        fx, fy = self.find(x), self.find(y)
        if fx == fy:
            return
        self.par[fx] = fy
        self.cnt -= 1


class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        n = len(grid)
        uf = UnionFind(4 * n * n)

        for i, seq in enumerate(grid):
            for j, ch in enumerate(seq):
                idx = (n * i + j) * 4
                up, right, down, left = idx, idx + 1, idx + 2, idx + 3
                if ch == '/':
                    uf.union(left, up)
                    uf.union(down, right)
                elif ch == '\\':
                    uf.union(up, right)
                    uf.union(left, down)
                elif ch == ' ':
                    uf.union(up, right)
                    uf.union(right, down)
                    uf.union(down, left)

                if j < n - 1:
                    uf.union(right, idx + 7)

                if i < n - 1:
                    uf.union(down, (n * (i + 1) + j) * 4)

        return uf.cnt


# @lc code=end

if __name__ == "__main__":
    solu = Solution()
    print(solu.regionsBySlashes([" /", "/ "]))
    print(solu.regionsBySlashes([" /", "  "]))
    print(solu.regionsBySlashes(["\\/", "/\\"]))
    print(solu.regionsBySlashes(["/\\", "\\/"]))
    print(solu.regionsBySlashes(["//", "/ "]))
