class Solution:
    def longestPalindrome(self, s: str) -> str:
            if   len(s)<=1:
                return s 
        
            def expantion(left,right) ->str:
                while left>=0 and right<len(s)and s[left]==s[right]:
                    left -=1
                    right +=1
                return s[left+1:right]
            longest_palindrome = ""
            for i in range(len(s)):
                p_1 = expantion(i,i)
                p_2 = expantion(i,i+1)

                if len(p_1) > len(longest_palindrome):
                    longest_palindrome = p_1
                if len(p_2) > len(longest_palindrome):
                    longest_palindrome = p_2
            return longest_palindrome



    
    
    
    
    
    




        