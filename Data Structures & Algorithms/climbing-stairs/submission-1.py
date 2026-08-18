class Solution:
    def climbStairs(self, n: int) -> int:
        dp ={}
        dp[1] =1
        dp[2]=2
        returnvalue = 0
        for i in range(3,n+1):
            dp[i] = dp[i-1]+dp[i-2]
            returnvalue = dp[i]
        if n>3:
            return returnvalue
        else:
            return n