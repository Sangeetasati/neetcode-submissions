class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = []
        for i, h in enumerate(heights):
            start = i
            while stack and h<stack[-1][1]:
                p_i, p_h = stack.pop()
                maxArea = max(maxArea, ((i - p_i) * p_h))
                start = p_i
            
            stack.append([start,h])
            
        for i in range(len(stack)):
            maxArea = max(maxArea, (len(heights) - stack[i][0])*stack[i][1])
        return maxArea
        


        
        