class Solution:
    def calculator(self,a:int,b:int,op:str):
         match op:
            case "+":
                return a+b
            case "-":
                return a-b
            case "*":
                return a*b
            case "/":
                return int(a / b)

    def evalRPN(self, tokens: List[str]) -> int:
        arr = []
        for i in tokens:
            if i not in  {"+", "-", "*", "/"}:
                arr.append(int(i))
            else:
                b = arr.pop()
                a =arr.pop()
                result = self.calculator(a,b,i)
                arr.append(result)
        return arr[0]
        
            