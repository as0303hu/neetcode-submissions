class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {"(":")",
                 "[":"]",
                "{":"}",
                }
        arr =[]
        for i in range(len(s)):
            if len(arr)>=1:
                ch = s[i]
                last_ele = arr[-1]
                matcher = pairs.get(last_ele,"")
                if matcher==ch:
                    arr.pop()
                else:
                    arr.append(ch)
            else:
                arr.append(s[i])
        print(arr)
        return False if arr else True