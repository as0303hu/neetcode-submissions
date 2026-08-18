class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            if num in freq:
                freq[num] +=1
            else:
                freq[num] = 1
        
        top_k = sorted(freq.items(),key=lambda item: item[1],reverse=True)[:k]        
        return [key for key, value in top_k]
