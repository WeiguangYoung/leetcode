/*
 * @Author: yangweiguang yangweiguang@uniml.com
 * @Date: 2023-05-05 14:12:20
 * @LastEditors: yangweiguang yangweiguang@uniml.com
 * @LastEditTime: 2023-05-05 14:12:23
 * @FilePath: /leetcode/1031/main.go
 * @Description:
 *
 * Copyright (c) 2023 by GuangjiTech, All Rights Reserved.
 */
package main

func maxSumTwoNoOverlap(nums []int, firstLen int, secondLen int) (ans int) {
	n := len(nums)
	s := make([]int, n+1)
	for i, x := range nums {
		s[i+1] = s[i] + x
	}
	for i, t := firstLen, 0; i+secondLen-1 < n; i++ {
		t = max(t, s[i]-s[i-firstLen])
		ans = max(ans, t+s[i+secondLen]-s[i])
	}
	for i, t := secondLen, 0; i+firstLen-1 < n; i++ {
		t = max(t, s[i]-s[i-secondLen])
		ans = max(ans, t+s[i+firstLen]-s[i])
	}
	return
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func main() {

}
