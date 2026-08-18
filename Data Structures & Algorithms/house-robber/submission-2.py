class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        dp_1 =0
        dp_2 =0
        for i  in range(n-1,-1,-1):
            curr =max(nums[i]+dp_2,dp_1)
            dp_2 = dp_1
            dp_1 = curr
        return dp_1