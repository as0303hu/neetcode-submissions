class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        
        dp_1 = 0
        dp_2 =0
        for i in range(n-1,0,-1):
            curr = max(nums[i]+dp_2,dp_1)
            dp_2 = dp_1
            dp_1 = curr
        case_1 = dp_1
        dp_1,dp_2 =0,0

        for i in range(n-2,-1,-1):
            curr = max(nums[i]+dp_2,dp_1)
            dp_2 = dp_1
            dp_1 = curr
        case_2 = dp_1
        return max(case_1,case_2)
        