class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        result = 0

        while left < right:
            # compute cur area
            area = min(heights[left], heights[right]) * (right - left)
            
            # update result with cur max area
            result = max(result, area)

            # move ptr to shorter line inward to find all possiblities
            if heights[left] <= heights[right]:
                left += 1
            else:
                right -= 1
        
        # return when ptrs meet
        return result