class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        s =0
        l =len(numbers)-1
        while s<l:
            total =numbers[s]+numbers[l]
            if total == target:
                return [s+1,l+1]
            elif(total>target):
                l -=1
            elif total<target:
                s +=1
            else:
                break
        return []
        