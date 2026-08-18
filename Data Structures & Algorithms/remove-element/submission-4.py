class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        array=[]
        for num in nums:
            if(num!=val):
                array.append(num)
        
        for i in range(len(array)):
            nums[i]=array[i]
        
        return len(array)