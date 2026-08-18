class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)

        dp1 = 0  # dp[i+1]
        dp2 = 0  # dp[i+2]

        for i in range(n - 1, -1, -1):
            curr = cost[i] + min(dp1, dp2)
            dp2 = dp1
            dp1 = curr

        return min(dp1, dp2)