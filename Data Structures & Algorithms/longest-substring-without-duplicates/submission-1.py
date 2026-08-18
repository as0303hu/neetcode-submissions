class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        u_s =""
        max_ch = 0
        for i in range(len(s)):
            if s[i] in u_s:
                index = 0
                for j in range(len(u_s)):
                    if s[i]==u_s[j]:     
                        if len(u_s)-1>=j:
                            u_s =u_s[j+1:] +s[i]
                        else:
                            u_s =s[i]
                        break
                        
            else:
                u_s = u_s + s[i]
            max_ch =max(max_ch,len(u_s))
        return max_ch
        