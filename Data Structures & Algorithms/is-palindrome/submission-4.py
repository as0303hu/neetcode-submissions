import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_text = "".join(ch.lower() for ch in s if ch.isalnum())
       
        p = len(clean_text)-1
        for i in range(len(clean_text)):
            if p<i:
                return True
            if not clean_text[i]==clean_text[p]:
                return False
            p -=1
        return True
            
       