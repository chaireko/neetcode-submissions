class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxArea = -1
        l,r=0,len(heights)-1
        while l < r:
            if min(heights[l], heights[r]) == heights[l]:
                maxArea = max(maxArea, heights[l]*(r-l))
            else:
                maxArea = max(maxArea, heights[r]*(r-l))
            if heights[l] <= heights[r]:
                l+=1
            else:
                r-=1
        return maxArea