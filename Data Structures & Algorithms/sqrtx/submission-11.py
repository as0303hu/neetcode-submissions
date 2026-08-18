class Solution:
    def mySqrt(self, x: int) -> int:
        if not x:
            return 0
        if x<=2:
            return 1
        start =1
        end = x
        middle = 0
        while(start<=end):
            middle = (start+end)//2
            value = middle*middle
            if value ==x:
                return middle
            elif value<x:
                start = middle+1
            elif  value>x:
                end = middle-1
        return start -1
        
        