class Solution:
    def maxArea(self, heights: List[int]) -> int:
        final_max =0
        last = len(heights)-1
        first =0
        while first<last:
            distance =last-first
            curr_max = min(heights[last],heights[first]) * distance
            final_max = max(final_max,curr_max)
            if(heights[last]>heights[first]):
                first +=1
            else:
                last -=1
        print(final_max)
        return final_max
        