class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        m_criteria = len(nums)/2
        freq_counter = {}
        for i in nums:
            if i in freq_counter:
                freq_counter[i] +=1
            else:
                freq_counter[i] =1
        
        for key in freq_counter:
            if(freq_counter[key] > m_criteria):
                return key