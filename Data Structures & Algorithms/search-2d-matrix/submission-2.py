class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        
        m = len(matrix)
        n= len(matrix[0])
        high =(m*n) -1
        start =0

        while start<=high:
            mid = (start+high)//2
            row = mid//n
            col = mid % n
            if matrix[row][col] ==target:
                return True
            if matrix[row][col]<target:
                start= mid+1
            if matrix[row][col]>target:
                high = mid -1
        return False