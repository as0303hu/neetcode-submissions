class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        ans = []
        for i in range(len(nums)):
            if(nums[i] not in ans):
                ans.append(nums[i])
            else:
                return True
        
        return False