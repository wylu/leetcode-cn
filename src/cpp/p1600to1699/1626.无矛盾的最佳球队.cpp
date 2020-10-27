/*
 * @lc app=leetcode.cn id=1626 lang=cpp
 *
 * [1626] 无矛盾的最佳球队
 *
 * https://leetcode-cn.com/problems/best-team-with-no-conflicts/description/
 *
 * algorithms
 * Medium (34.60%)
 * Likes:    20
 * Dislikes: 0
 * Total Accepted:    2.2K
 * Total Submissions: 6.3K
 * Testcase Example:  '[1,3,5,10,15]\n[1,2,3,4,5]'
 *
 * 假设你是球队的经理。对于即将到来的锦标赛，你想组合一支总体得分最高的球队。球队的得分是球队中所有球员的分数 总和 。
 * 
 * 然而，球队中的矛盾会限制球员的发挥，所以必须选出一支 没有矛盾 的球队。如果一名年龄较小球员的分数 严格大于
 * 一名年龄较大的球员，则存在矛盾。同龄球员之间不会发生矛盾。
 * 
 * 给你两个列表 scores 和 ages，其中每组 scores[i] 和 ages[i] 表示第 i 名球员的分数和年龄。请你返回
 * 所有可能的无矛盾球队中得分最高那支的分数 。
 * 
 * 
 * 
 * 示例 1：
 * 
 * 输入：scores = [1,3,5,10,15], ages = [1,2,3,4,5]
 * 输出：34
 * 解释：你可以选中所有球员。
 * 
 * 示例 2：
 * 
 * 输入：scores = [4,5,6,5], ages = [2,1,2,1]
 * 输出：16
 * 解释：最佳的选择是后 3 名球员。注意，你可以选中多个同龄球员。
 * 
 * 
 * 示例 3：
 * 
 * 输入：scores = [1,2,3,5], ages = [8,9,10,1]
 * 输出：6
 * 解释：最佳的选择是前 3 名球员。
 * 
 * 
 * 
 * 
 * 提示：
 * 
 * 
 * 1 <= scores.length, ages.length <= 1000
 * scores.length == ages.length
 * 1 <= scores[i] <= 10^6
 * 1 <= ages[i] <= 1000
 * 
 * 
 */

/**
 * @File    :   1626.无矛盾的最佳球队.cpp
 * @Time    :   2020/10/27 23:06:00
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 * 本题的数据范围显然不可能支持我们进行所有子集的枚举。我们希望找到一种顺序，
 * 使得我们在进行选择时，总是不会发生冲突。
 * 
 * 我们可以将所有队员按照年龄升序进行排序，年龄相同时，则按照分数升序进行排序。
 * 排序之后，我们可以进行动态规划。令 dp[i] 表示最后一个队员是第 i 个队员时
 * 的最大分数（这里的 i 是重新排序后的编号）。我们只需要在 [0,i-1] 的范围内
 * 枚举上一个队员即可。这里，如果上一个队员的分数不超过当前队员的分数，就可以
 * 进行转移。
 * 
 * 为什么这样的枚举一定是合法的呢？因为我们的最大分数总是在最后一个队员处取得
 * （对于相同年龄的，我们是按照分数升序排序的，所以分数较高的一定在更后面），
 * 同时第 i 个队员的年龄不小于之前任意队员的年龄，所以只要第 i 个队员的分数
 * 大于等于之前的分组中最后一个队员的分数，就一定可以将第 i 个队员加入到组里，
 * 从而得到一个以第 i 个队员为最后一名队员的新的组。
 * 
 * 复杂度
 * 
 * 时间复杂度 O(N^2)
 * 空间复杂度 O(N)
 */

#include <bits/stdc++.h>
using namespace std;

// @lc code=start
class Solution {
public:
    int bestTeamScore(vector<int>& scores, vector<int>& ages) {
        int ans = 0, n = scores.size();
        vector<pair<int, int>> players;
        for (int i = 0; i < n; i++) {
            players.emplace_back(ages[i], scores[i]);
        }
        sort(players.begin(), players.end());

        vector<int> dp(n);
        for (int i = 0; i < n; i++) {
            dp[i] = players[i].second;
            for (int j = 0; j < i; j++) {
                if (players[j].second <= players[i].second) {
                    dp[i] = max(dp[i], dp[j] + players[i].second);
                }
            }
            ans = max(ans, dp[i]);
        }

        return ans;
    }
};
// @lc code=end

int main(int argc, char const* argv[]) {
    Solution solu;
    vector<int> scores = {4, 5, 6, 5};
    vector<int> ages = {2, 1, 2, 1};
    cout << solu.bestTeamScore(scores, ages) << endl;
    return 0;
}
