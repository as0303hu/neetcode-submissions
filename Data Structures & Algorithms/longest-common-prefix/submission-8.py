class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
    
        str_length = len(strs[0])
        for i in range(0,str_length):
            for string in strs:
                if (not string):
                    return ""

                if(not len(string)>i or strs[0][i]!=string[i]):
                    if(i>0):
                        return string[0:i]
                    return ""
                    
        return strs[0]      
        
            
        