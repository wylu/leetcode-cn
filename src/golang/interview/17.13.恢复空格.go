package interview

/**
 * @File    :   17.13.恢复空格.go
 * @Time    :   2020/07/09 21:48:28
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 * Dynamic Programming
 *
 * State:
 *   dp[i]: 表示前i个字符(即s[0:i])最少的未识别的字符数量
 *
 * Initial State:
 *   dp[0] = 0
 *   dp[i] = dp[i-1] + 1, 1 <= i <= n
 *
 * State Transition:
 *   每次转移时，考虑 s[j] 到 s[i-1] 组成的子串（即 sentence[j:i]）是否能在词典
 *   中找到，如果能找到:
 *     dp[i] = min(dp[i], dp[j])
 *   否则，可以复用 dp[i−1] 的状态再加上当前未被识别的 s[i-1] (第 i 个字符)，
 *   此时有:
 *     dp[i] = dp[i-1] + 1
 */
func respace(dictionary []string, sentence string) int {
	dict := make(map[string]bool, len(dictionary))
	for _, word := range dictionary {
		dict[word] = true
	}

	st, n := []byte(sentence), len(sentence)
	dp := make([]int, n+1)
	for i := 1; i <= n; i++ {
		dp[i] = dp[i-1] + 1
		for j := 0; j < i; j++ {
			key := string(st[j:i])
			if _, ok := dict[key]; ok {
				dp[i] = min(dp[i], dp[j])
			}
		}
	}
	return dp[n]
}

func min(x, y int) int {
	if x < y {
		return x
	}
	return y
}
