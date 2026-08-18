from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_freq = Counter(s1)
        match_freq = {}
        l=0

        for r in range(len(s2)):
            ch = s2[r]
            match_freq[ch]= match_freq.get(ch,0)+1
            if s1_freq ==match_freq:
                return True
            if r-l>=len(s1)-1:
                if s2[l] in match_freq:
                    if match_freq[s2[l]]>1:
                         match_freq[s2[l]] -= 1
                    else:
                        del match_freq[s2[l]]
                l +=1
            
        return False            


        