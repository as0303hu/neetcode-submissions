class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        c_p = prices[0]
        max_profit = 0
        for i in range(1,len(prices)):
            if prices[i]<c_p:
                c_p = prices[i]
            else:
                max_profit= max(max_profit,prices[i]-c_p)

        return max_profit  