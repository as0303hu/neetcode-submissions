class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        c_count = {}
        l=0
        max_c_count =0
        max_length = 0
        for r in range(len(s)):
            ch = s[r]
            c_count[ch]=c_count.get(ch,0)+1
            max_c_count = max(max_c_count,c_count[ch])
            if(r-l+1)-max_c_count>k:
                c_count[s[l]] -=1
                l+=1
            max_length = max(max_length,r-l+1)
        return max_length
        