class Solution:
    def countSubstrings(self, s: str) -> int:
        n =len(s)
        count =0
        def expantions(start,end):
            nonlocal count
            while start>=0 and end<n and s[start]==s[end]:
                count +=1
                start-=1
                end +=1
        
        for i in range(n):
            expantions(i,i)
            expantions(i,i+1)
        return count
        