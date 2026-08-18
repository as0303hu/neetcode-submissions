class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        arr = []
        for i in tokens:
            if i not in  {"+", "-", "*", "/"}:
                arr.append(int(i))
            else:
                match i:
                    case "+":
                        numer_2 = arr.pop()
                        numer_1 = arr.pop()
                        result = numer_2 + numer_1
                        arr.append(result)
                    case "-":
                        numer_2 = arr.pop()
                        numer_1 = arr.pop()
                        result = numer_1 -numer_2
                        arr.append(result)
                    case "*":
                        numer_2 = arr.pop()
                        numer_1 = arr.pop()
                        result = numer_2 * numer_1
                        arr.append(result)
                    case "/":
                        numer_2 = arr.pop()
                        numer_1 = arr.pop()
                        result = int(numer_1 / numer_2)
                        arr.append(result)
        return arr[0]
        
            