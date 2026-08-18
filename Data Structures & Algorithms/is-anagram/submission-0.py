class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_length = len(s)
        t_length = len(t)
        freq_count = {}

        if(s_length != t_length):
            return False

        for val in s:
            if val in freq_count:
                freq_count[val] +=1
            else:
                freq_count[val] =1

        for v in t:
            if v not in freq_count or freq_count[v]<=0:
                return False
            else:
                freq_count[v]-=1
        
        for val in freq_count:
            if(freq_count[val] != 0):
                return False
        return True