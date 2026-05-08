class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # initialze output array with 0s
        result = [0] * len(temperatures)

        # use monotonic stack storing -> every addition is cooler than the previous
        temp_stack = []

        for i, temp in enumerate(temperatures):
            # if cur temp is warmer than top of stack, found the next warmer day
            while temp_stack and temp > temp_stack[-1][0]:
                stackT, stackInd = temp_stack.pop()

                # calculate ith number of days 
                result[stackInd] = i - stackInd
            
            # otherwise, push onto stack -> warmer day not found yet
            temp_stack.append((temp, i))
        
        return result
        