class Solution:
    def maxArea(self, heights: List[int]) -> int:
        unit = 0
        l = 0
        r = len(heights) - 1 
        while l<r:
            area = (r-l) * min(heights[l], heights[r]) 
            unit = max(unit, area)
            if heights[l] < heights[r]:
                l +=1
            else:
                r -=1
        return unit

    #    unit = 0
    #    max(unit, min(1,7) * (7-0) ) = 7
    #    max(7, min(1,7) * (7-0) ) = 7


    #     [1,7,2,5,4,7,3,6]
            # max(unit, min(heights[0]=1, height[7]=6) * (7-0) ) = 7
            # max(unit, min(heights[1]=7, height[7]=6) * (7-1) ) = 36




    #        1 2 3 4 5 6 7
    #          2 10 12 28 12 30
    #            2 4 3